#!/usr/bin/env python3
"""
Extract red scatter points from monomer conversion vs time plot (140°C).

Approach:
1. Detect the plot area (axes bounding box) by finding the black axis lines/frame.
2. Detect red scatter points using HSV color thresholding.
3. Convert pixel coordinates to data coordinates using known axis ranges:
   X: 0 ~ 2000 s
   Y: 0 ~ 1 (conversion)
4. Mark detected points on the original image for verification.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json

# ── Paths ────────────────────────────────────────────────────────────────
IMG_PATH = Path("/home/admin/books/polymerization/kinetics/pmma/geleffect/high-temperature-mma-polymerization-nising2004/images/fig3 monomer conversion evolution-140℃.png")
OUT_DIR = Path("/home/admin/books/polymerization/kinetics/pmma/geleffect/high-temperature-mma-polymerization-nising2004")

# Known axis ranges
X_MIN, X_MAX = 0, 2000    # time (s)
Y_MIN, Y_MAX = 0, 1       # conversion X


def detect_plot_bounds_bgr(bgr):
    """
    Detect the plot area bounding box by finding significant black lines
    (axes frame) in the image.

    Strategy:
    - Convert to grayscale
    - Threshold to find dark pixels (axes, frame, text)
    - Use horizontal and vertical projection profiles to find the main
      axis lines that form the rectangular plot boundary.
    - Specifically look for the longest continuous dark horizontal and
      vertical lines near the expected plot region.
    """
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape

    # Binary: dark pixels (axes lines, text) are white
    _, dark = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

    # ── Horizontal projection: find top and bottom axis lines ──
    h_proj = np.sum(dark, axis=1).astype(np.float64)

    # The axis lines will have high projection values.
    # We look for the top-most and bottom-most strong horizontal lines
    # that are in reasonable regions.
    # Smooth the projection slightly
    from scipy.ndimage import uniform_filter1d
    h_smooth = uniform_filter1d(h_proj, size=5)

    # Find peaks in horizontal projection (rows with many dark pixels)
    # Threshold: rows with more than 30% of width as dark pixels
    h_thresh = w * 0.25
    candidate_rows = np.where(h_smooth > h_thresh)[0]

    if len(candidate_rows) < 2:
        # Fallback: use looser threshold
        h_thresh = w * 0.10
        candidate_rows = np.where(h_smooth > h_thresh)[0]

    # Group contiguous rows into "lines"
    groups = []
    if len(candidate_rows) > 0:
        start = candidate_rows[0]
        prev = candidate_rows[0]
        for r in candidate_rows[1:]:
            if r - prev > 3:
                groups.append((start, prev))
                start = r
            prev = r
        groups.append((start, prev))

    # Filter: keep groups with decent width
    groups = [(s, e) for s, e in groups if e - s >= 1]

    print(f"  Horizontal line candidates (row ranges): {groups}")

    # Top axis: first strong line in the upper half
    # Bottom axis: last strong line in the lower half
    mid_row = h // 2
    top_groups = [(s, e) for s, e in groups if e < mid_row]
    bottom_groups = [(s, e) for s, e in groups if s > mid_row]

    if top_groups:
        top_bound = top_groups[-1][1]  # bottom edge of top axis line
    else:
        top_bound = int(h * 0.05)

    if bottom_groups:
        bottom_bound = bottom_groups[0][0]  # top edge of bottom axis line
    else:
        bottom_bound = int(h * 0.95)

    # ── Vertical projection: find left and right axis lines ──
    v_proj = np.sum(dark, axis=0).astype(np.float64)
    v_smooth = uniform_filter1d(v_proj, size=5)

    v_thresh = h * 0.25
    candidate_cols = np.where(v_smooth > v_thresh)[0]

    if len(candidate_cols) < 2:
        v_thresh = h * 0.10
        candidate_cols = np.where(v_smooth > v_thresh)[0]

    col_groups = []
    if len(candidate_cols) > 0:
        start = candidate_cols[0]
        prev = candidate_cols[0]
        for c in candidate_cols[1:]:
            if c - prev > 3:
                col_groups.append((start, prev))
                start = c
            prev = c
        col_groups.append((start, prev))

    col_groups = [(s, e) for s, e in col_groups if e - s >= 1]
    print(f"  Vertical line candidates (col ranges): {col_groups}")

    mid_col = w // 2
    left_groups = [(s, e) for s, e in col_groups if e < mid_col]
    right_groups = [(s, e) for s, e in col_groups if s > mid_col]

    if left_groups:
        left_bound = left_groups[-1][1]  # right edge of left axis line
    else:
        left_bound = int(w * 0.05)

    if right_groups:
        right_bound = right_groups[0][0]  # left edge of right axis line
    else:
        right_bound = int(w * 0.95)

    return top_bound, bottom_bound, left_bound, right_bound


def detect_red_scatter_points(bgr, top, bottom, left, right):
    """
    Detect red scatter points within the plot area using HSV color thresholding.

    Red in HSV: hue near 0° (or near 180°), high saturation, high value.
    We look for solid red circles (markers).

    Returns list of (col, row) pixel coordinates.
    """
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    # Crop to plot area
    plot_hsv = hsv[top:bottom, left:right]

    # Red hue wraps around in HSV: low hues (0-10) and high hues (170-180)
    # Lower red range
    lower_red1 = np.array([0, 100, 80])
    upper_red1 = np.array([12, 255, 255])
    mask1 = cv2.inRange(plot_hsv, lower_red1, upper_red1)

    # Upper red range
    lower_red2 = np.array([170, 100, 80])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(plot_hsv, lower_red2, upper_red2)

    red_mask = mask1 | mask2

    # Also try RGB-based detection as a complement
    plot_bgr = bgr[top:bottom, left:right]
    # Red: R dominates over G and B
    r, g, b_chan = plot_bgr[:, :, 2].astype(np.float64), plot_bgr[:, :, 1].astype(np.float64), plot_bgr[:, :, 0].astype(np.float64)
    # Red pixels: R > 150, R > 1.5*G, R > 1.5*B
    rgb_red = (r > 130) & (r > 1.3 * g) & (r > 1.3 * b_chan)
    rgb_red_mask = rgb_red.astype(np.uint8) * 255

    # Combine masks
    combined = red_mask | rgb_red_mask

    # Clean up with morphological operations
    kernel = np.ones((2, 2), np.uint8)
    combined = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel)
    combined = cv2.morphologyEx(combined, cv2.MORPH_OPEN, kernel)

    # Find connected components (each should be a scatter point)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(combined, connectivity=8)

    points = []
    print(f"\n  Found {num_labels - 1} red connected components in plot area")

    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        cx, cy = centroids[i]

        # Filter by area: scatter points should be reasonable size
        # (not tiny noise, not huge red regions)
        if 4 <= area <= 800:
            # Convert back to full image coordinates
            abs_x = cx + left
            abs_y = cy + top
            points.append((abs_x, abs_y))
            print(f"    Point {len(points)}: pixel=({abs_x:.1f}, {abs_y:.1f}), area={area}")

    return points


def pixel_to_data(px, py, top, bottom, left, right):
    """
    Convert pixel coordinates to data coordinates.

    Pixel y increases downward, data y increases upward.
    """
    x_data = X_MIN + (px - left) / (right - left) * (X_MAX - X_MIN)
    y_data = Y_MIN + (bottom - py) / (bottom - top) * (Y_MAX - Y_MIN)
    return x_data, y_data


def main():
    print("=" * 60)
    print("Red Scatter Point Extraction from Monomer Conversion Plot")
    print("=" * 60)

    # ── Load image ──
    bgr = cv2.imread(str(IMG_PATH))
    if bgr is None:
        # Try with alpha
        img_rgba = cv2.imread(str(IMG_PATH), cv2.IMREAD_UNCHANGED)
        if img_rgba is not None:
            bgr = img_rgba[:, :, :3]
        else:
            raise FileNotFoundError(f"Cannot load image: {IMG_PATH}")

    h, w = bgr.shape[:2]
    print(f"\nImage size: {w} x {h}")

    # ── Step 1: Detect plot bounds ──
    print("\n[1] Detecting plot area boundaries...")
    top, bottom, left, right = detect_plot_bounds_bgr(bgr)
    print(f"\n  Detected plot bounds:")
    print(f"    Top   : row {top}")
    print(f"    Bottom: row {bottom}")
    print(f"    Left  : col {left}")
    print(f"    Right : col {right}")
    print(f"    Plot size: {right - left} x {bottom - top} pixels")

    # ── Step 2: Detect red scatter points ──
    print("\n[2] Detecting red scatter points...")
    points_px = detect_red_scatter_points(bgr, top, bottom, left, right)
    print(f"\n  Total candidate points: {len(points_px)}")

    # ── Step 3: Convert to data coordinates ──
    print("\n[3] Converting to data coordinates...")
    data_points = []
    for px, py in points_px:
        x_d, y_d = pixel_to_data(px, py, top, bottom, left, right)
        data_points.append((x_d, y_d))
        print(f"    Pixel ({px:.1f}, {py:.1f}) → Data ({x_d:.1f} s, {y_d:.4f})")

    # Sort by x
    data_points.sort(key=lambda p: p[0])

    print(f"\n  ── Final {len(data_points)} Data Points (sorted by time) ──")
    print(f"  {'Time (s)':>10s}  {'Conversion':>12s}")
    print(f"  {'─'*10}  {'─'*12}")
    for x_d, y_d in data_points:
        print(f"  {x_d:10.1f}  {y_d:12.6f}")

    # ── Step 4: Save data ──
    output_json = OUT_DIR / "extracted_points_140C.json"
    with open(output_json, 'w') as f:
        json.dump({
            "description": "Monomer conversion vs time at 140°C",
            "x_label": "time (s)",
            "y_label": "conversion X",
            "x_range": [X_MIN, X_MAX],
            "y_range": [Y_MIN, Y_MAX],
            "plot_bounds_px": {"top": int(top), "bottom": int(bottom), "left": int(left), "right": int(right)},
            "points": [{"time_s": float(round(x, 1)), "conversion": float(round(y, 6))} for x, y in data_points]
        }, f, indent=2)
    print(f"\n  Data saved to: {output_json}")

    # ── Step 5: Verification - mark points on original image ──
    print("\n[4] Creating verification image...")

    # Use matplotlib to overlay on the original image with correct coordinate system
    # Load image via matplotlib for consistent coordinate handling
    from PIL import Image
    pil_img = Image.open(str(IMG_PATH))
    img_array = np.array(pil_img)

    fig, ax = plt.subplots(1, 1, figsize=(14, 11))

    # Display the original image
    ax.imshow(img_array)

    # Mark the detected plot bounds
    rect = plt.Rectangle(
        (left, top), right - left, bottom - top,
        fill=False, edgecolor='cyan', linewidth=2, linestyle='--'
    )
    ax.add_patch(rect)

    # Mark the detected red points
    for i, (px, py) in enumerate(points_px):
        ax.plot(px, py, 'o', markersize=12, markerfacecolor='none',
                markeredgecolor='lime', markeredgewidth=2.5)
        ax.annotate(
            f"#{i+1}\n({data_points[i][0]:.0f}s, {data_points[i][1]:.3f})",
            (px + 15, py - 15),
            fontsize=8, color='white', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.7),
        )

    ax.set_xlim(0, w)
    ax.set_ylim(h, 0)  # Invert y-axis to match image coordinates
    ax.set_title("Verification: Detected Red Scatter Points\nMonomer Conversion vs Time @ 140°C", fontsize=14)
    ax.set_xlabel("Pixel X")
    ax.set_ylabel("Pixel Y")
    ax.legend(["Detected Plot Bounds", "Detected Red Points"], loc='lower right')

    output_png = OUT_DIR / "verification_140C.png"
    fig.savefig(str(output_png), dpi=150, bbox_inches='tight')
    print(f"  Verification image saved to: {output_png}")

    # ── Step 6: Also create a clean data plot ──
    print("\n[5] Creating data plot...")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    times = [p[0] for p in data_points]
    convs = [p[1] for p in data_points]

    ax2.plot(times, convs, 'ro-', markersize=10, markerfacecolor='red',
             markeredgecolor='darkred', linewidth=2)
    ax2.set_xlim(X_MIN, X_MAX)
    ax2.set_ylim(Y_MIN, Y_MAX)
    ax2.set_xlabel("Time (s)", fontsize=12)
    ax2.set_ylabel("Conversion X", fontsize=12)
    ax2.set_title("Extracted Data: Monomer Conversion vs Time @ 140°C", fontsize=14)
    ax2.grid(True, alpha=0.3)

    for i, (t, c) in enumerate(data_points):
        ax2.annotate(f"({t:.0f}, {c:.4f})", (t, c),
                     textcoords="offset points", xytext=(10, -15),
                     fontsize=8, color='darkred')

    output_data_png = OUT_DIR / "extracted_data_plot_140C.png"
    fig2.savefig(str(output_data_png), dpi=150, bbox_inches='tight')
    print(f"  Data plot saved to: {output_data_png}")

    plt.show()
    print("\nDone!")


if __name__ == "__main__":
    main()
