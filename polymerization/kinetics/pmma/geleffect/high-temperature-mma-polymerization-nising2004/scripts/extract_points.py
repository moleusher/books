#!/usr/bin/env python3
"""
Extract blue scatter points from the MMA polymerization conversion chart.

Axis bounds (pixel coordinates):
  Y-axis (x=0):   col 212.5
  Right (x=2000): col 1059
  Top (y=1):      row 28.5
  Bottom (y=0):   row 703.5
"""
import cv2
import numpy as np
import csv
import os

# Paths
img_path = "/home/admin/books/polymerization/kinetics/pmma/geleffect/high-temperature-mma-polymerization-nising2004/images/fig3 monomer conversion evolution-180℃.png"
output_dir = "/home/admin/.claude/skills/chartdigitizer/workspace/iteration-1/eval-1/without_skill/outputs"
os.makedirs(output_dir, exist_ok=True)

# ---- 1. Load image ----
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Cannot load image: {img_path}")

print(f"Image loaded: {img.shape}")

# ---- 2. Create HSV mask for blue points ----
# Blue scatter points: BGR=(204,72,63), HSV ~(118,176,204)
# H-range for blue: 100-135, generous S and V thresholds
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define blue range in HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([135, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# ---- 3. Find contours and filter by area ----
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

min_area = 30  # filter noise
valid_contours = [c for c in contours if cv2.contourArea(c) > min_area]
print(f"Found {len(valid_contours)} blue scatter points (contours > {min_area} px)")

# Compute centroids from valid contours
points_pixel = []
for c in valid_contours:
    M = cv2.moments(c)
    if M["m00"] > 0:
        cx = M["m10"] / M["m00"]  # column (pixel x)
        cy = M["m01"] / M["m00"]  # row (pixel y)
        points_pixel.append((cx, cy))

print(f"Extracted {len(points_pixel)} centroids")

# ---- 4. Convert pixel to data coordinates ----
# Axis bounds
x0_px = 212.5   # col at x=0
x1_px = 1059.0  # col at x=2000
y1_px = 28.5    # row at y=1  (top)
y0_px = 703.5   # row at y=0  (bottom)

x_range_px = x1_px - x0_px  # 846.5 px for 2000 s
y_range_px = y0_px - y1_px  # 675 px for 1.0 conversion

x_scale = 2000.0 / x_range_px
y_scale = 1.0 / y_range_px

# Filter: only include points whose centroid is strictly inside the plot area
# (excludes axis labels/tick marks outside the frame)
points_data = []
for cx, cy in points_pixel:
    # Check if inside plot area (with a small margin to avoid boundary pixels)
    if cx < x0_px + 2 or cx > x1_px - 2 or cy < y1_px + 2 or cy > y0_px - 2:
        print(f"  Skipping point outside plot area: ({cx:.1f}, {cy:.1f})")
        continue
    x_data = (cx - x0_px) * x_scale
    y_data = (cy - y0_px) * (-y_scale)  # image y is inverted
    # Clamp to valid range
    x_data = max(0, min(2000, x_data))
    y_data = max(0, min(1, y_data))
    points_data.append((x_data, y_data, cx, cy))

# Sort by x (time)
points_data.sort(key=lambda p: p[0])

print(f"\nExtracted {len(points_data)} data points:")
for x, y, cx, cy in points_data:
    print(f"  t={x:7.1f}s  X={y:.4f}  (px: {cx:.1f}, {cy:.1f})")

# ---- 5. Save CSV ----
csv_path = os.path.join(output_dir, "extracted_data.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Time (s)", "Conversion X"])
    for x, y, _, _ in points_data:
        writer.writerow([f"{x:.1f}", f"{y:.4f}"])
print(f"\nSaved: {csv_path}")

# ---- 6. Save verification image ----
# Draw on a copy: circles at detected centroids, plus the data value labels
vis = img.copy()

# Draw the mask region for reference (using addWeighted to maintain contiguous array)
mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
green_overlay = np.zeros_like(vis, dtype=np.uint8)
green_overlay[mask > 0] = (0, 200, 0)
vis_detected = cv2.addWeighted(vis, 0.6, green_overlay, 0.4, 0)

# Mark centroids with red circles
for cx, cy, _, _ in points_data:
    cv2.circle(vis_detected, (int(cx), int(cy)), 5, (0, 0, 255), -1)
    # Draw a small cross
    cv2.drawMarker(vis_detected, (int(cx), int(cy)), (0, 255, 255), cv2.MARKER_CROSS, 8, 1)

# Draw axis frame for reference
cv2.rectangle(vis_detected, (int(x0_px), int(y1_px)), (int(x1_px), int(y0_px)), (255, 0, 255), 1)

verif_path = os.path.join(output_dir, "verification.png")
cv2.imwrite(verif_path, vis_detected)
print(f"Saved: {verif_path}")

print("\nDone!")
