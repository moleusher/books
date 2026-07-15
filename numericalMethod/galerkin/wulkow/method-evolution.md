# Wulkow 离散 Galerkin 方法文献演化谱系

> 跨度 1989–2021，共 10 篇独立文献（14 个目录中 3 篇有重复副本，1 篇不相关），
> 记录从数学理论 → 算法实现 → 工业软件 → 跨学科扩展的完整演化路径。

---

## 文献总表

| # | 目录 | 年份 | 作者 | 标题 |
|---|------|------|------|------|
| 1 | sc-88-06 / polykin-orthog / wulkow1996-discrete-galerkin | 1989 | Deuflhard, Wulkow | Computational Treatment of Polyreaction Kinetics by Orthogonal Polynomials of a Discrete Variable |
| 2 | countable-ode | 1990 | Wulkow | Numerical Treatment of Countable Systems of ODEs (博士论文) |
| 3 | sc-90-15 / wulkow1990-polyreactions-development | 1990 | Wulkow, Ackermann | Numerical Simulation of Macromolecular Kinetics – Recent Developments |
| 4 | macron | 1990 | Ackermann, Wulkow | MACRON – A Program Package for Macromolecular Kinetics |
| 5 | sc-91-17 | 1991 | Wulkow | Adaptive Treatment of Polyreactions in Weighted Sequence Spaces |
| 6 | adaptive-dg | ~1992–1993 | Deuflhard, Ackermann | Adaptive Discrete Galerkin Methods for Macromolecular Processes |
| 7 | mwd-sim | 1995/1996 | Wulkow | The Simulation of Molecular Weight Distributions in Polyreaction Kinetics by Discrete Galerkin Methods |
| 8 | chem-master-eq | 2007 | Deuflhard, Huisinga, Jahnke, Wulkow | Adaptive Discrete Galerkin Methods Applied to the Chemical Master Equation |
| 9 | hybrid-gm | 2010 | Schütte, Wulkow | A Hybrid Galerkin–Monte-Carlo Approach to Higher-Dimensional Population Balances in Polymerization Kinetics |
| 10 | predici | 2021 | Kandelhard, Georgopanos | Predici as a Polymer Engineers' Tool for the Synthesis of Polymers via Anionic Polymerization |

**重复副本：**
- `polykin-orthog` = `sc-88-06`（相同论文）
- `wulkow1996-discrete-galerkin` 目录内容 = `sc-88-06`（目录名有误导性，内容为 1989 年论文）
- `wulkow1990-polyreactions-development` = `sc-90-15`（相同论文）

**不相关：** `optscheme` — 炼油分馏工艺文档，不含 Wulkow、Galerkin 或聚合相关内容。

---

## 第一阶段：奠基 — 离散 Galerkin 方法的诞生 (1989)

### SC-88-06 — 离散 Galerkin 方法的开创性论文
> Deuflhard & Wulkow, *Computational Treatment of Polyreaction Kinetics by Orthogonal Polynomials of a Discrete Variable* (1989)
> Konrad-Zuse-Zentrum für Informationstechnik Berlin, SC-88-06

**核心贡献：** 首次提出**离散 Galerkin 方法**。核心思想：

- 将聚合度（链长）视为**离散变量**而非连续变量——这是与当时所有竞争方法的根本区别
- 构造与合理选择的概率密度函数关联的**离散内积**
- Schulz-Flory 分布 → **离散 Laguerre 多项式**
- Poisson 分布 → **Charlier 多项式**
- 以 Galerkin 投影替代对百万级 ODE 的直接刚性积分

**对比的竞争方法：**
1. 统计矩方法 — 截断指数选择无解
2. 连续 PDE 方法 — 将离散变量连续化引入不适定性

> 🔑 **奠基性创新：** 在加权序列空间中做 Galerkin 逼近，用正交多项式作为基函数，将无限维问题投影到有限维子空间。

---

## 第二阶段：理论体系化 & 双路径分化 (1990–1991)

### countable-ode — 博士论文：完整的数学理论
> Wulkow, *Numerical Treatment of Countable Systems of Ordinary Differential Equations* (1990年12月)
> Konrad-Zuse-Zentrum für Informationstechnik Berlin, TR-90-8

**核心贡献：** CODEX 算法背后的**完整数学理论框架**：

1. 可数 ODE 系统 (CODE) 在**双参数加权序列空间** $H_{\rho,\alpha}$ 中的理论
2. 修正离散 Laguerre 多项式的构造与逼近性质
3. 时间离散化与外推（Rothe 方法）
4. 稳态子问题的 Galerkin 投影与近似解
5. **多层求积算法** (SUMMATOR) — 解析性质不可用时的数值预处理
6. 基于渐近展开的**自适应权函数拟合**

> 🔑 **理论支柱：** Rothe 方法（先时间离散 → 再 Galerkin 空间离散）是后来所有发展的数学基础。

### SC-90-15 — 双路线综述
> Wulkow & Ackermann, *Numerical Simulation of Macromolecular Kinetics – Recent Developments* (1990年11月, IUPAC Working Party)

**核心贡献：** 首次公开综述两条技术路线：

1. **MACRON 路线 (Method of Lines, MOL)：** 先 Galerkin 空间离散（移动基函数展开）→ 再数值积分展开系数对应的 ODE。易于理解，适合工程应用。
2. **CODEX 路线 (Rothe Method, ROM)：** 先时间离散（外时间离散化）→ 再 Galerkin 解稳态子问题。双参数权函数族。更灵活可靠，但尚未广泛实现。

> 🔑 **路径分叉点：** MOL（先空间后时间）vs ROM（先时间后空间）——这一选择在 2007 年的 CME 论文中重新成为核心论题。

### MACRON — 第一个软件包
> Ackermann & Wulkow, *MACRON – A Program Package for Macromolecular Kinetics* (1990年12月)

**核心贡献：** 将 Method of Lines 方案工程化为**可工业使用的 FORTRAN 软件包**：

- **化学编译器：** 用户以化学反应式语法输入，自动完成 Galerkin 预处理
- 内置复杂数值例程（ODE 求解器、稳定求积、误差控制）
- 用户无需了解数值方法细节
- 局限：最适用于与 Schulz-Flory 分布相关的反应体系

> 🔑 **工程化里程碑：** 从算法到软件包，"化学反应式 → 模拟结果"的自动化。

### SC-91-17 — CODEX 全自适应算法
> Wulkow, *Adaptive Treatment of Polyreactions in Weighted Sequence Spaces* (1991年12月)

**核心贡献：** CODEX 路线的完整自适应实现：

- 在加权序列空间 $H_{\rho,\alpha}$ 中建立 CODEs 的完备理论
- 修正离散 Laguerre 多项式 + **Gauss 型求积**
- **权函数拟合**实现自适应基函数选择
- **全自适应：** 时间步长 + 截断指数 + 权函数参数均自动调节
- 数值算例：链加成聚合、聚合物降解、烟灰生成

> 🔑 **理论完备化：** 从"能用"到"自适应地用"，CODEX 成为方法论的参考实现。

---

## 第三阶段：综述与整合 (1992–1996)

### adaptive-dg — 方法论全貌综述
> Deuflhard & Ackermann, *Adaptive Discrete Galerkin Methods for Macromolecular Processes* (~1992–1993)

**核心贡献：** 以综述形式呈现离散 Galerkin 方法的完整图景：

- 两种变体的系统比较：MOL（MACRON 风格）vs ROM/CODEX 风格
- 离散 Hilbert 空间尺度（加权序列空间）的构造
- 自适应截断指数的控制与监测
- 算例扩展至生态领域：**Alcaligenes eutrophus 细菌的 PHB 生物聚合/降解**

> 🔑 **教育性综述：** 将 1989–1992 的技术进展整合为可理解的统一框架。

### mwd-sim — PREDICI：工业级 h-p 方法
> Wulkow, *The Simulation of Molecular Weight Distributions in Polyreaction Kinetics by Discrete Galerkin Methods* (投稿 1995年11月, 发表 1996)
> *Macromolecular Theory and Simulations*

**核心贡献：** 综合此前所有理论成果，提出**离散 Galerkin h-p 方法**并实现为商业软件 **PREDICI**：

- **h-adaptivity：** 自适应选择基函数个数（截断指数）
- **p-adaptivity：** 自适应选择权函数参数（分布形状）
- C++ 实现，PC 可运行，速度提升约 $10^4$ 倍
- 全面支持：任意反应类型、链长依赖速率常数、无稳态假设

设计目标（全部实现）：
- 任意数量的物种和链长分布
- 任意反应步骤
- 对分子量分布形态无限制
- 不需要模型简化（如稳态假设）

> 🔑 **集大成：** 1989–1995 七年的理论积累收敛为单一算法框架 + 商业软件产品。

---

## 第四阶段：跨学科扩展 — 化学主方程 (2007)

### chem-master-eq — 从聚合动力学到系统生物学
> Deuflhard, Huisinga, Jahnke, Wulkow, *Adaptive Discrete Galerkin Methods Applied to the Chemical Master Equation* (2007年4月)

**核心贡献：** 将离散 Galerkin 方法从聚合动力学**迁移到系统生物学**的化学主方程 (CME)：

- 揭示 CME 的**离散 PDE 结构**
- 关键方法论决策：**Rothe 方法 (ROM) vs MOL**
  - Engblom (2006) 独立重新发现了离散 Galerkin 思想，但选择了 MOL
  - 本文从理论和算法角度**论证 ROM 的优越性**（动态状态空间自适应）
- 引入**离散 Chebyshev 多项式**作为新正交基
- 提出**张量积方法**处理多维状态空间（基因调控网络、信号通路）
- **Gauss-Christoffel 求积**高效计算矩阵元和右端项
- 算例：双稳态 Toggle Switch、挑战性测试问题

> 🔑 **跨学科迁移：** 聚合动力学中发展了 18 年的方法论被系统生物学独立"重新发现"。该文从理论上证明了 ROM 路线在自适应能力上优于 MOL——解决了 1990 年 MACRON vs CODEX 路线的最终裁决。

---

## 第五阶段：混合方法 & 工业验证 (2010–2021)

### hybrid-gm — 确定性方法 + Monte-Carlo 融合
> Schütte & Wulkow, *A Hybrid Galerkin–Monte-Carlo Approach to Higher-Dimensional Population Balances in Polymerization Kinetics* (2010)
> *Macromolecular Theory and Simulations*, 19(6)

**核心贡献：** 突破单一方法的局限，提出**确定性+随机混合算法**：

- **链长维度 → 确定性离散 Galerkin (PREDICI h-p 方法)：** 高效、精确、可微
- **其他属性维度（支化度、组成等）→ Monte-Carlo 采样：** 通用、灵活
- **理论耦合基础：** 从化学主方程 (CME) 出发，链长分布是概率分布的**第一边际矩**
- 优势：
  - MC 粒子数大为减少（链长方差由确定性部分承担）
  - 反应速率从确定性结果中获得，精度高
  - 比纯 MC 高效，比纯确定性方法信息更丰富

> 🔑 **方法论融合：** 精度与通用性不再对立——GRAD 范式（Galerkin + RAndom + Deterministic）。

### predici — 30 年后的工业验证
> Kandelhard & Georgopanos, *Predici as a Polymer Engineers' Tool for the Synthesis of Polymers via Anionic Polymerization* (2021)
> *Industrial & Engineering Chemistry Research*, 60, 11373–11384

**核心贡献：** PREDICI 的**工业应用案例**（非方法论文献）：

- 阴离子聚合苯乙烯/异戊二烯共聚的**工艺放大**
- 将 PREDICI 的反应动力学模型与**传热模型**耦合
- 预测安全关键参数（温度曲线、压力曲线）
- 研究工艺参数与产品性质的相互作用

> 🔑 **终点验证：** 30 余年后，工业用户论文证明了方法的持久实用价值——从 ZIB 技术报告到工程师日常工具。

---

## 演化路径图

```
1989  SC-88-06          ─── 离散 Galerkin 方法诞生
       (polykin-orthog)       正交多项式 + 离散内积
      ┌─────────────────────────────────────────┐
      │                                         │
1990  countable-ode        SC-90-15             │
      (博士论文/理论)       (双路线综述)          │
      Rothe 方法           MOL vs Rothe          │
      │                    │                    │
1990  │                    MACRON                │
      │                    (MOL 软件包/FORTRAN)   │
      │                    │                    │
1991  SC-91-17             │                    │
      (CODEX 全自适应)      │                    │
      └────────┬───────────┘                    │
               │                                │
~1992          adaptive-dg                      │
               (综述：方法论全貌)                 │
               │                                │
1995           mwd-sim                          │
               PREDICI h-p 方法 ← 两路线融合     │
               C++ 商业软件                      │
               │                                │
2007           chem-master-eq                   │
               (跨学科：系统生物学 CME)            │
               ROM > MOL 最终裁决                │
               │                                │
2010           hybrid-gm                        │
               (方法论融合：Galerkin + MC)        │
               │                                │
2021           predici                          │
               (工业验证：阴离子聚合放大)           │
```

---

## 方法论演化主线

| 维度 | 演化轨迹 |
|------|---------|
| **离散化策略** | MOL (先空间) → Rothe (先时间) → h-p (双自适应) |
| **正交基** | Laguerre / Charlier → 修正 Laguerre → Chebyshev (CME) |
| **权函数** | 固定 (Schulz-Flory) → 双参数族 $H_{\rho,\alpha}$ → 自适应拟合 |
| **软件形态** | 研究代码 → MACRON (MOL, FORTRAN) → CODEX (ROM) → **PREDICI** (h-p, C++ 商业) |
| **问题维度** | 1D (链长) → 2D (链长+属性, 张量积) → 高维 (hybrid MC) |
| **应用领域** | 聚合动力学 → 生态/烟灰生成 → 系统生物学 (CME) → 工业放大 |
| **速度提升** | 直接积分不可行 → MACRON (可行) → PREDICI ($\sim 10^4\times$) |

---

## 关键参考文献

| 编号 | 文献 |
|------|------|
| [8] | Deuflhard, Wulkow (1989). Computational Treatment of Polyreaction Kinetics by Orthogonal Polynomials of a Discrete Variable. *ZIB SC-88-06*. |
| [9] | Wulkow (1990). Numerical Treatment of Countable Systems of Ordinary Differential Equations. *ZIB TR-90-8* (PhD Thesis). |
| [11] | Wulkow, Ackermann (1990). Numerical Simulation of Macromolecular Kinetics – Recent Developments. *ZIB SC-90-15*. |
| [12] | Ackermann, Wulkow (1990). MACRON – A Program Package for Macromolecular Kinetics. *ZIB SC-90-19*. |
| — | Wulkow (1991). Adaptive Treatment of Polyreactions in Weighted Sequence Spaces. *ZIB SC-91-17*. |
| — | Deuflhard, Ackermann (~1992–1993). Adaptive Discrete Galerkin Methods for Macromolecular Processes. *ZIB SC-92-??* |
| [14] | Wulkow (1996). The Simulation of Molecular Weight Distributions in Polyreaction Kinetics by Discrete Galerkin Methods. *Macromol. Theory Simul.* |
| — | Deuflhard, Huisinga, Jahnke, Wulkow (2007). Adaptive Discrete Galerkin Methods Applied to the Chemical Master Equation. |
| [15] | Schütte, Wulkow (2010). A Hybrid Galerkin–Monte-Carlo Approach... *Macromol. Theory Simul.*, 19(6). |
| — | Kandelhard, Georgopanos (2021). Predici as a Polymer Engineers' Tool... *Ind. Eng. Chem. Res.*, 60, 11373–11384. |

---

*生成日期：2026-07-15 · 源文件位于 `numericalMethod/galerkin/wulkow/method-evolution.md`*
