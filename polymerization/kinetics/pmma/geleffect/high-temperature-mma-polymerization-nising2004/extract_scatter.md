基于我们二次对同一类型科研图表（不同颜色实心点）的提取实践，初步总结了一套**通用、可复用的 Python 图像数据提取方法、流程与代码结构**。

这种方法的核心思想是：**利用计算机视觉（OpenCV）定位像素坐标，通过坐标轴的像素边界建立从“像素空间”到“物理空间”的线性映射关系。**

---

### 一、 核心方法：基于空间映射与颜色过滤

我们不依赖复杂的深度学习 OCR（识别文字），而是采用经典的图像处理与几何映射：

1.  **特征提取**：利用 **HSV 颜色空间** 过滤掉背景、线条和文字，只保留目标颜色（红色、绿色、蓝色等）的散点。
2.  **中心定位**：计算散点色块轮廓的**质心（Centroid）**，获取其在图像上的像素坐标 `(px, py)`。
3.  **坐标定义**：手动提取图表黑色边框的**像素坐标范围** `[x_min, x_max]` 和 `[y_min, y_max]`。
4.  **线性映射**：根据原图 X轴 和 Y轴的**物理极值**，建立简单的线性方程将像素坐标还原为真实物理数据（注意 Y轴图像向下、物理向上的翻转）。

---

### 二、 标准工作流程 (Workflow)

在实际提取新图表时，请遵循以下 6 个步骤：

1.  **图像输入与预处理**：
    *   读取彩色图像。
    *   (可选) 调整图像分辨率，若分辨率极高，需先缩小以防OpenCV处理过慢。
2.  **确定目标颜色阈值（核心关键）**：
    *   将 BGR 转为 HSV 色域。 **不要用 RGB**，因为 RGB 对光照敏感，而 HSV 能精准锁定色相（Hue）。
    *   *调试技巧*：使用像素颜色拾取器（如 Windows 自带的画图工具，或在线 HSV 提取工具），点击目标散点获取具体的 `H, S, V` 值，然后在代码中设置 `lower` 和 `upper` 包围它。
3.  **提取轮廓与过滤**：
    *   使用 `cv2.findContours` 找轮廓。
    *   **必须加入面积过滤** `if cv2.contourArea(cnt) > 30:`，以防将轴的刻度线噪点、压缩伪影误识别为散点。
4.  **定标：寻找坐标轴边界（必须人工微调）**：
    *   提取原图中包围数据的**黑色细边框**的像素坐标。
    *   将 4 个常数写在代码顶部，方便调试。
    *   *验证技巧*：在生成的验证图中，用 `cv2.rectangle` 画出这个边界框，检查是否与原图的黑边完美重合。
5.  **计算物理坐标（映射）**：
    *   \(物理X = X_{min} + \frac{像素X - 像素X_{min}}{像素宽度} \times 物理宽度\)
    *   \(物理Y = Y_{max} - \frac{像素Y - 像素Y_{min}}{像素高度} \times 物理高度\) *(注意这里是减号，因为图像像素坐标系 Y轴向下，而物理坐标系 Y轴向上)*。
6.  **输出与验证**：
    *   保存为 `.csv` 表格。
    *   使用 `matplotlib` 绘制提取的散点图，并与原图进行形状和趋势比对。

---

### 三、 代码结构模板 (可复用的函数式架构)

下面的代码是高度模块化的，你以后遇到此类图表，**只需修改“配置区”的参数即可**，无需改动核心算法。

```python
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================= 1. 配置参数区 (每次提取新图表只需修改此区) =================
INPUT_IMAGE = 'input.png'          # 输入图片路径
OUTPUT_CSV = 'extracted_data.csv'  # 输出CSV路径
OUTPUT_VERIFY = 'verify_result.png' # 验证图路径

# 1.1 目标颜色的 HSV 阈值 (需根据具体图片调整)
# 绿色示例: [35, 50, 50] ~ [85, 255, 255]
# 蓝紫色示例: [100, 80, 80] ~ [135, 255, 255]
LOWER_COLOR = np.array([35, 50, 50]) 
UPPER_COLOR = np.array([85, 255, 255])

# 1.2 轮廓面积过滤 (排除小噪点，保留实心点)
MIN_AREA = 30 

# 1.3 坐标轴边界像素值 (最关键：需保证蓝框与原图黑边重合)
# 建议在第一次运行后，根据生成的 verify 图进行微调
PX_X_MIN, PX_X_MAX = 140, 848
PX_Y_MIN, PX_Y_MAX = 38, 152

# 1.4 物理坐标系极值
PHY_X_MIN, PHY_X_MAX = 0.0, 2000.0
PHY_Y_MIN, PHY_Y_MAX = 0.0, 1.0
# ============================================================================

def extract_points(img_path, out_csv, out_verify):
    # 1. 读取图片
    img = cv2.imread(img_path)
    if img is None:
        return print("错误：图片未找到")

    # 2. 颜色分离与掩膜
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)

    # 3. 提取轮廓与中心
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    pixel_points = []
    
    for cnt in contours:
        if cv2.contourArea(cnt) < MIN_AREA:
            continue
        # 获取质心 (像素坐标)
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            pixel_points.append((cx, cy))
            
    pixel_points.sort(key=lambda p: p[0]) # 按 X 轴排序

    # 4. 像素与物理坐标换算
    px_width = PX_X_MAX - PX_X_MIN
    px_height = PX_Y_MAX - PX_Y_MIN
    phy_width = PHY_X_MAX - PHY_X_MIN
    phy_height = PHY_Y_MAX - PHY_Y_MIN

    data = []
    valid_pixels = []
    
    for px, py in pixel_points:
        # 边界过滤：防止识别到坐标轴标签上的杂色
        if not (PX_X_MIN <= px <= PX_X_MAX and PX_Y_MIN <= py <= PX_Y_MAX):
            continue
            
        phy_x = PHY_X_MIN + ((px - PX_X_MIN) / px_width) * phy_width
        # Y轴翻转计算
        phy_y = PHY_Y_MAX - ((py - PX_Y_MIN) / px_height) * phy_height
        
        data.append([phy_x, phy_y])
        valid_pixels.append((px, py))

    # 5. 保存数据
    df = pd.DataFrame(data, columns=['Time [s]', 'Conversion X [-]'])
    df.to_csv(out_csv, index=False)
    print(f"成功提取 {len(df)} 个点，数据已保存至 {out_csv}")

    # 6. 绘制验证图
    img_verify = img.copy()
    for px, py in valid_pixels:
        cv2.circle(img_verify, (px, py), 8, (0, 255, 0), 2) # 识别框
        cv2.circle(img_verify, (px, py), 2, (0, 0, 255), -1) # 中心点

    # 画出用来换算的边界框
    cv2.rectangle(img_verify, (PX_X_MIN, PX_Y_MIN), (PX_X_MAX, PX_Y_MAX), (255, 0, 0), 2)
    cv2.imwrite(out_verify, img_verify)
    print(f"验证图已生成：{out_verify}")

    # 7. Matplotlib 绘图验证
    plt.figure()
    plt.xlim(PHY_X_MIN, PHY_X_MAX)
    plt.ylim(PHY_Y_MIN, PHY_Y_MAX)
    plt.scatter(df['Time [s]'], df['Conversion X [-]'])
    plt.title('Extracted Data Check')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    extract_points(INPUT_IMAGE, OUTPUT_CSV, OUTPUT_VERIFY)
```

### 四、实践中的错误与正确做法对比

以下是在两次实际提取（140°C 红色散点、160°C 绿色散点）中踩过的坑和最终的正确方案。

---

#### 4.1 坐标轴边界的确定

| | ❌ 错误做法 | ✅ 正确做法 |
|---|---|---|
| **方法** | 凭肉眼猜测像素边界值。例如第一次设 `pixel_y_max=150`，而实际 X 轴在 row 703——差了 550 像素，导致 8 个散点中 7 个被当作"界外"丢弃。 | 逐行/逐列扫描暗像素，精确定位轴线：`np.sum(gray[row, :] < 80)` 统计每行的黑色像素数，峰值即为轴线位置。 |
| **案例** | 设定 `pixel_x_min=142, pixel_y_max=150`，结果只捕获到 1 个点。 | 扫描发现 Y 轴在 col 212-213（669 个暗像素），X 轴在 row 703-704（847 个暗像素）。 |
| **精度** | 用整数近似。如 `pixel_x_min=213`。 | 用浮点数精确定位轴线中心。如 `pixel_x_min=212.5`（col 212 和 213 的中心）。因为第一个散点恰好在轴线中心（px=212.5），用整数会导致 ~0.5px 偏差。|
| **验证** | 不检查边界框是否与原图黑边对齐。 | 在验证图上绘制蓝色边界矩形，目视确认与轴线重合。 |

**扫描轴线的诊断代码模板：**

```python
# 寻找 Y 轴（左竖线）——扫描每一列，统计暗像素
for c in range(50, 400):
    dark_count = np.sum(gray[30:750, c] < 80)
    if dark_count > 400:  # 贯穿大部分高度的黑线
        print(f"Y-axis at col {c}: {dark_count} dark pixels")

# 寻找 X 轴（下横线）——扫描每一行
for r in range(650, h - 50):
    dark_count = np.sum(gray[r, 150:1150] < 80)
    if dark_count > 400:
        print(f"X-axis at row {r}: {dark_count} dark pixels")
```

---

#### 4.2 面积过滤：区分散点与噪声

| | ❌ 错误做法 | ✅ 正确做法 |
|---|---|---|
| **过滤策略** | 不过滤或仅靠边界框过滤。 | 用 `cv2.contourArea(cnt)` 计算每个轮廓面积，设定阈值（如 `> 30`）。 |
| **案例** | 140°C 图像检测到 118 个红色轮廓，其中 110 个是坐标轴文字、刻度线、JPEG 压缩伪影，面积均为 0。 | 过滤后精确得到 8 个真散点（面积 82~256）。160°C 图像从 15 个候选中筛出 9 个真散点（面积 117~250）。 |
| **后果** | 如果不加面积过滤，116 个噪声点会全部进入边界检查逻辑，且大部分因在界外被 SKIP，输出充斥噪音日志。 | 干净输出：每个轮廓的面积、中心坐标一目了然。 |

**关键代码：**
```python
MIN_AREA = 30  # 实心散点通常 > 50 px²
for cnt in contours:
    if cv2.contourArea(cnt) < MIN_AREA:
        continue  # 跳过噪点
```

---

#### 4.3 颜色空间选择

| | ❌ 错误做法 | ✅ 正确做法 |
|---|---|---|
| **颜色模型** | 使用 RGB/BGR 阈值。条件如 `R > 130 and R > 1.3*G and R > 1.3*B` 需要多个关系判断，且对光照/压缩敏感。 | 使用 HSV 颜色空间。只需设定色相（Hue）范围，饱和度和明度给宽范围即可。 |
| **红色** | — | 红色在 HSV 中跨两端：`[0, 100, 100]~[10, 255, 255]` 和 `[160, 100, 100]~[180, 255, 255]`，需要两个 mask 合并。 |
| **绿色** | — | 绿色在 HSV 中连续：`[35, 80, 80]~[85, 255, 255]`，一个 mask 即可。 |

**实际提取到的散点 BGR 值（用于验证）：**
- 140°C 红色：BGR = (36, 28, 237) — 几乎纯红
- 160°C 绿色：BGR = (76, 177, 34) — 几乎纯绿

---

#### 4.4 边界容差：处理轴线上的点

| | ❌ 错误做法 | ✅ 正确做法 |
|---|---|---|
| **边界检查** | 硬边界 `px < pixel_x_min or px > pixel_x_max`。第一个散点恰好在轴线中心，px=211.0 比 pixel_x_min=212.5 小 1.5px，被拒绝。 | 加入容差 margin：`px < pixel_x_min - MARGIN`，允许 ±4px。 |
| **案例** | 160°C 第一个点 (211.0, 706.5) 在 Y 轴左侧 1.5px，被 SKIP。 | 加 `MARGIN=4` 后全部 9 个点通过。第一个点转换后为 (-3.5s, 0.008)，本质是 (0, 0)。 |
| **教训** | 容差不影响坐标映射精度——散点中心 1~2px 的偏差在物理坐标中对应 < 5s（范围 2000s），可忽略。 | 坐标映射公式仍用精确的轴线位置（212.5），边界检查则用容差放宽。两者解耦。 |

---

#### 4.5 同一模板的多图复用

两次提取的关键发现：**同一论文的同一类图表，轴线位置完全相同。**

| 参数 | 140°C 图 | 160°C 图 |
|---|---|---|
| 图片尺寸 | 1186×942 | 1186×942 |
| Y 轴 (x=0) | col 212-213 | col 212-213 |
| X 轴 (y=0) | row 703-704 | row 703-704 |
| 上边框 (y=1) | row 28-29 | row 28-29 |
| 右边框 (x=2000) | col 1059 | col 1059 |

> **推论**：提取同一论文的其他子图时（如 180°C），可直接复用这组边界参数，只需调整目标颜色阈值。

---

#### 4.6 质心计算方式的选择

| 方法 | 适用场景 | 本次评估 |
|---|---|---|
| `cv2.minAreaRect(cnt)[0]` | 任意形状的最小外接矩形中心 | 对正方形散点效果与质心相同 |
| `cv2.moments(cnt)` → 质心 | 任意形状的亮度加权中心 | **推荐**——更精确，尤其对不规则色块 |
| 直接取轮廓的 `boundingRect` 中心 | 矩形 | 精度稍差，不推荐 |

本次实际使用 `cv2.moments` 计算质心。

---

### 五、最终提取结果

#### 140°C（红色散点，8 个点）

| Time (s) | Conversion |
|----------|------------|
| 0.0 | 0.0007 |
| 215.0 | 0.1815 |
| 282.3 | 0.2326 |
| 419.4 | 0.2948 |
| 582.4 | 0.4133 |
| 894.3 | 0.6148 |
| 1018.3 | 0.8541 |
| 1596.0 | 0.9733 |

#### 160°C（绿色散点，9 个点）

| Time (s) | Conversion |
|----------|------------|
| ~0 | 0.0081 |
| 187.8 | 0.2899 |
| 282.5 | 0.3777 |
| 367.5 | 0.4640 |
| 503.5 | 0.5819 |
| 647.6 | 0.7971 |
| 751.5 | 0.8937 |
| 967.6 | 0.9179 |
| 1302.0 | 0.9230 |

---

### 六、总结

| 维度 | 要点 |
|---|---|
| **颜色检测** | HSV 优于 RGB；红色需双区间；始终用面积过滤排除噪点 |
| **轴定位** | 扫描暗像素比肉眼估算准；用浮点数记录轴线中心；加 ±4px 容差 |
| **验证** | 必须生成验证图（蓝框 + 标记点）；第一个点应接近 (0, 0) |
| **复用** | 同论文同模板图表，轴线参数可直接复用 |
| **效率** | 每次提取运行 < 1 秒，无需 GPU，通用性强 |