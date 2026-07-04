#!/usr/bin/env python3
"""
Extract green scatter points from monomer conversion vs time plot (160°C).
Same method as 140°C: HSV color filtering + axis boundary calibration.
"""

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────
IMG_PATH = Path("/home/admin/books/polymerization/kinetics/pmma/geleffect/high-temperature-mma-polymerization-nising2004/images/fig3 monomer conversion evolution-160℃.png")
OUT_DIR = Path("/home/admin/books/polymerization/kinetics/pmma/geleffect/high-temperature-mma-polymerization-nising2004/data/conversion-time-160")

def extract_points(image_path, output_csv_path, verification_image_path):
    # 1. Load image
    img = cv2.imread(str(image_path))
    if img is None:
        print("Error: cannot load image.")
        return

    h, w = img.shape[:2]
    print(f"Image size: {w} x {h}")

    # 2. Extract green scatter points via HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Green hue: ~40-80 in OpenCV HSV (0-180)
    lower_green = np.array([35, 80, 80])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    cv2.imwrite(str(OUT_DIR / "debug_mask.png"), mask)

    # 3. Find contours, filter by area
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print(f"\nFound {len(contours)} green contours (before filtering)")
    pixel_points = []

    MIN_AREA = 20
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < MIN_AREA:
            continue
        M = cv2.moments(cnt)
        if M['m00'] > 0:
            cx = M['m10'] / M['m00']
            cy = M['m01'] / M['m00']
        else:
            rect = cv2.minAreaRect(cnt)
            cx, cy = rect[0]
        print(f"  center=({cx:.1f}, {cy:.1f}), area={area:.1f}")
        pixel_points.append((cx, cy))

    pixel_points.sort(key=lambda p: p[0])
    print(f"\nAfter area filter (>{MIN_AREA}): {len(pixel_points)} points")

    # 4. Axis boundaries (same layout as 140°C image)
    #   - Left Y-axis: col 212-213 → center 212.5 = x=0
    #   - Right frame: col 1059 → x=2000
    #   - Top frame: row 28-29 → center 28.5 = y=1
    #   - Bottom X-axis: row 703-704 → center 703.5 = y=0
    pixel_x_min = 212.5   # x=0
    pixel_x_max = 1059    # x=2000
    pixel_y_max = 712     # y=0 (enough margin for first point)
    pixel_y_min = 29      # y=1

    # Tolerance margin for boundary check (px)
    MARGIN = 4

    # 5. Physical coordinate ranges
    phys_x_min, phys_x_max = 0.0, 2000.0
    phys_y_min, phys_y_max = 0.0, 1.0

    # 6. Coordinate conversion
    pixel_width = pixel_x_max - pixel_x_min
    pixel_height = pixel_y_max - pixel_y_min
    phys_width = phys_x_max - phys_x_min
    phys_height = phys_y_max - phys_y_min

    converted_data = []
    final_points = []

    for px, py in pixel_points:
        if (px < pixel_x_min - MARGIN or px > pixel_x_max + MARGIN or
            py < pixel_y_min - MARGIN or py > pixel_y_max + MARGIN):
            print(f"  SKIP: ({px:.1f}, {py:.1f}) outside bounds")
            continue

        phys_x = phys_x_min + ((px - pixel_x_min) / pixel_width) * phys_width
        phys_y = phys_y_max - ((py - pixel_y_min) / pixel_height) * phys_height

        converted_data.append([phys_x, phys_y])
        final_points.append((px, py))

    print(f"\nExtracted green scatter points: {len(converted_data)}")

    # 7. Save CSV
    df = pd.DataFrame(converted_data, columns=['Time [s]', 'Conversion X [-]'])
    df.to_csv(str(output_csv_path), index=False)
    print(f"Data saved to: {output_csv_path}")
    print(df)

    # 8. Verification image (mark points on original)
    img_verify = img.copy()
    for px, py in final_points:
        cv2.circle(img_verify, (int(px), int(py)), 8, (0, 255, 0), 2)   # green circle
        cv2.circle(img_verify, (int(px), int(py)), 3, (0, 0, 255), -1)  # red center dot

    cv2.rectangle(img_verify, (int(pixel_x_min), int(pixel_y_min)),
                  (int(pixel_x_max), int(pixel_y_max)), (255, 0, 0), 2)
    cv2.imwrite(str(verification_image_path), img_verify)
    print(f"Verification image saved to: {verification_image_path}")

    # 9. Clean data plot
    plt.figure(figsize=(8, 6))
    plt.xlim(phys_x_min, phys_x_max)
    plt.ylim(phys_y_min, phys_y_max)
    plt.scatter(df['Time [s]'], df['Conversion X [-]'], color='green', marker='s',
                s=80, edgecolors='darkgreen', label='Extracted 160°C')
    plt.xlabel('Time [s]')
    plt.ylabel('Conversion X [-]')
    plt.title('Extracted Data: Monomer Conversion vs Time @ 160°C')
    plt.grid(True, alpha=0.3)
    plt.legend()
    data_plot_path = OUT_DIR / "extracted_data_plot.png"
    plt.savefig(str(data_plot_path), dpi=150, bbox_inches='tight')
    print(f"Data plot saved to: {data_plot_path}")
    plt.close()


if __name__ == '__main__':
    extract_points(
        IMG_PATH,
        OUT_DIR / "extracted_data.csv",
        OUT_DIR / "verification_result.png"
    )
