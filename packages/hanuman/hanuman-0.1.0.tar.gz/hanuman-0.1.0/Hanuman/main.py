#!/usr/bin/env python
# coding: utf-8

"""
Hanuman - Typhoon Animation Generator
Author: CZHanoi
In memory of a friend of Hinnamnor.
"""

import csv
import cv2
import numpy as np
from datetime import datetime, timedelta
from collections import OrderedDict
import math
from tqdm import tqdm  # Progress bar library
import argparse
import os

###############################################################################
# 1. Configuration
###############################################################################
# Default file names
DEFAULT_CSV_FILE = "typhoon202411.csv"  # IBTrACS CSV with '\ufeffSID' + second line unit row
DEFAULT_WORLD_MAP_FILE = "world_map.png"  # 21600x10800 equirectangular map
DEFAULT_OUTPUT_VIDEO = "typhoon_season_a13.mp4"

# NW Pacific cropping range: lon[100,180], lat[0,45] (width 80°, height 45°, 16:9)
NW_MIN_LAT = 0.0
NW_MAX_LAT = 45.0
NW_MIN_LON = 100.0
NW_MAX_LON = 180.0

# Output canvas size (16:9)
CROP_WIDTH = 1280
CROP_HEIGHT = 720

# Frames per 3 hours interpolation => originally 60 -> changed to 15 => animation speed x4
FRAMES_PER_3H = 15
# Video frame rate
FPS = 30

# Typhoon icon base size (scaled by 1.5x)
TY_ICON_RADIUS = 24

# If a typhoon reached C1+ and the last point latitude >=22 => change to EX
EX_THRESHOLD_LAT = 22.0

# When there are no typhoons, time progresses at 25x speed
EMPTY_SPEEDUP_FACTOR = 25

# Add static frames after the video ends (10 seconds * FPS)
STATIC_FRAMES_AFTER_END = 10 * FPS


###############################################################################
# 2. Utility Functions: Loading Images, Coordinate Transformation, CSV Parsing, Interpolation, etc.
###############################################################################
def load_world_map(filepath):
    """
    Load the world map image.
    """
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Cannot load map file: {filepath}")
    return img


def latlon_to_world_xy(lat, lon, world_w, world_h):
    """
    Equirectangular projection:
    x: 0→world_w corresponds to lon: 0→360
    y: 0→world_h corresponds to lat: +90→-90 (top→bottom)
    """
    x_ratio = lon / 360.0
    y_ratio = (90.0 - lat) / 180.0
    x = int(x_ratio * world_w)
    y = int(y_ratio * world_h)
    return x, y


def crop_nw_pacific(world_img, nw_min_lat, nw_max_lat, nw_min_lon, nw_max_lon, crop_width, crop_height):
    """
    Crop the world map to the NW Pacific region and resize.
    """
    h, w, _ = world_img.shape

    x1, y1 = latlon_to_world_xy(nw_max_lat, nw_min_lon, w, h)  # Top-left
    x2, y2 = latlon_to_world_xy(nw_min_lat, nw_max_lon, w, h)  # Bottom-right
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    crop = world_img[y1:y2, x1:x2]
    if crop.size == 0:
        raise ValueError("Cropping area is empty. Please check NW_* parameters.")

    crop = cv2.resize(crop, (crop_width, crop_height), interpolation=cv2.INTER_AREA)
    return crop


def latlon_to_crop_xy(lat, lon, world_w, world_h, nw_min_lat, nw_max_lat, nw_min_lon, nw_max_lon, crop_width,
                      crop_height):
    """
    Map (lat, lon) to cropped (0..CROP_WIDTH, 0..CROP_HEIGHT)
    """
    x1, y1 = latlon_to_world_xy(nw_max_lat, nw_min_lon, world_w, world_h)
    x2, y2 = latlon_to_world_xy(nw_min_lat, nw_max_lon, world_w, world_h)
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1

    wx, wy = latlon_to_world_xy(lat, lon, world_w, world_h)
    cx = wx - x1
    cy = wy - y1
    cw = x2 - x1
    ch = y2 - y1
    if cw <= 0 or ch <= 0:
        return 0, 0

    xr = cx / float(cw)
    yr = cy / float(ch)
    final_x = int(xr * crop_width)
    final_y = int(yr * crop_height)
    return final_x, final_y


def get_category_by_wind(intensity):
    """
    Determine typhoon category based on 1-minute average wind speed (knots).
    """
    if intensity < 34:
        return "TD"
    elif intensity < 64:
        return "TS"
    elif intensity < 83:
        return "C1"
    elif intensity < 96:
        return "C2"
    elif intensity < 113:
        return "C3"
    elif intensity < 137:
        return "C4"
    else:
        return "C5"


def parse_typhoon_data(csv_file, ex_threshold_lat):
    """
    Parse the typhoon data CSV file.

    Steps:
    1. Remove BOM with 'utf-8-sig' encoding.
    2. Skip the second row (unit row).
    3. Retain only BASIN=WP.
    4. Parse time, lat, lon, wind => category.
    5. If a typhoon reached C1+ and the last point latitude >=22, change the last point category to EX.
    """
    storms = {}
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        print("Header (after removing BOM):", reader.fieldnames)

        line_idx = 0
        for row in reader:
            line_idx += 1
            # Skip the second row (unit row)
            if line_idx == 1:
                print("Skipping unit row:", row)
                continue

            sid = row.get("SID", "").strip()
            if not sid:
                continue
            if row.get("BASIN", "") != "WP":
                continue

            time_str = row.get("ISO_TIME", "").strip()
            if not time_str:
                continue

            # Parse time
            t = None
            fmts = ["%m/%d/%Y %H:%M", "%m/%d/%Y %H:%M:%S",
                    "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"]
            for fmt in fmts:
                try:
                    t = datetime.strptime(time_str, fmt)
                    break
                except:
                    pass
            if not t:
                continue

            try:
                lat = float(row["LAT"])
                lon = float(row["LON"])
            except:
                continue
            if lon < 0:
                lon += 360

            # Read WMO_WIND or USA_WIND
            w_str = row.get("WMO_WIND", "").strip()
            if not w_str or w_str == "-1":
                w_str = row.get("USA_WIND", "0")
            try:
                wind = float(w_str)
            except:
                wind = 0.0

            cat = get_category_by_wind(wind)
            name = row.get("NAME", "NONAME").strip()
            if name == "":
                name = "NONAME"

            storms.setdefault(sid, []).append({
                'time': t,
                'lat': lat,
                'lon': lon,
                'intensity': wind,
                'cat': cat,
                'name': name
            })

    # Sort by time and check for C1+ => EX
    for sid, track in storms.items():
        track.sort(key=lambda x: x['time'])
        # Check if it ever reached C1+
        ever_c1_plus = any(pt['cat'] in ("C1", "C2", "C3", "C4", "C5") for pt in track)
        if track and ever_c1_plus:
            if track[-1]['lat'] >= ex_threshold_lat:
                track[-1]['cat'] = "EX"
    return storms


###############################################################################
# 3. Drawing Functions: Colors, Icons, Time Circle
###############################################################################
def multi_segment_color(val):
    """
    Multi-segment gradient:
    0=Blue (TD),
    25=Light Blue (TS at 25 kt),
    34=Green (TS),
    64=Yellow (C1),
    100=Orange (C2),
    150=Purple (C3-C5)
    """
    segments = [
        (0, (255, 0, 0)),  # Blue (TD)
        (25, (255, 255, 0)),  # Light Blue (TS at 25 kt)
        (34, (0, 255, 0)),  # Green (TS)
        (64, (0, 255, 255)),  # Yellow (C1)
        (100, (0, 165, 255)),  # Orange (C2)
        (150, (128, 0, 128)),  # Purple (C3-C5)
    ]
    if val < segments[0][0]:
        return segments[0][1]
    if val > segments[-1][0]:
        return segments[-1][1]
    for i in range(len(segments) - 1):
        v0, c0 = segments[i]
        v1, c1 = segments[i + 1]
        if v0 <= val <= v1:
            alpha = (val - v0) / float(v1 - v0 + 1e-9)
            b = int(c0[0] + alpha * (c1[0] - c0[0]))
            g = int(c0[1] + alpha * (c1[1] - c0[1]))
            r = int(c0[2] + alpha * (c1[2] - c0[2]))
            return (b, g, r)
    return segments[-1][1]


def draw_typhoon_icon(img, x, y, intensity, cat, angle_deg, name, ty_icon_radius):
    """
    Draw the typhoon icon at (x, y) with specified intensity and category.
    """
    base_color = multi_segment_color(intensity)
    radius = ty_icon_radius

    # Circle
    cv2.circle(img, (x, y), radius, base_color, -1)

    # Draw symmetric arcs based on category
    lvl = 0
    if cat.startswith("C"):
        try:
            lvl = int(cat[1])
        except:
            lvl = 5
    elif cat == "EX":
        lvl = 0  # Do not draw arcs

    for i in range(lvl):
        # Draw first side of the arc
        r_arc = radius + 8 + 4 * i
        start_angle = (angle_deg + i * 30) % 360
        end_angle = (start_angle + 60) % 360
        arc_col = tuple(int(0.5 * c) for c in base_color)

        # Check if the arc needs to be split
        if end_angle < start_angle:
            # Split into two parts
            cv2.ellipse(img, (x, y), (r_arc, r_arc), 0, start_angle, 360, arc_col, 1, cv2.LINE_AA)
            cv2.ellipse(img, (x, y), (r_arc, r_arc), 0, 0, end_angle, arc_col, 1, cv2.LINE_AA)
        else:
            cv2.ellipse(img, (x, y), (r_arc, r_arc), 0, start_angle, end_angle, arc_col, 1, cv2.LINE_AA)

        # Draw the symmetric second side of the arc
        start_angle_sym = (start_angle + 180) % 360
        end_angle_sym = (end_angle + 180) % 360

        if end_angle_sym < start_angle_sym:
            cv2.ellipse(img, (x, y), (r_arc, r_arc), 0, start_angle_sym, 360, arc_col, 1, cv2.LINE_AA)
            cv2.ellipse(img, (x, y), (r_arc, r_arc), 0, 0, end_angle_sym, arc_col, 1, cv2.LINE_AA)
        else:
            cv2.ellipse(img, (x, y), (r_arc, r_arc), 0, start_angle_sym, end_angle_sym, arc_col, 1, cv2.LINE_AA)

    # Write category at the center
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, cat, (x - 12, y + 6), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, cat, (x - 12, y + 6), font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    # Write name at the top-right corner of the icon
    cv2.putText(img, name, (x + radius + 2, y - radius), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, name, (x + radius + 2, y - radius), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


def draw_time_circle(base, t_cur, time_circle_params):
    """
    Draw a time progress circle at the bottom-left corner.
    """
    cx, cy, radius = time_circle_params

    # Progress of the day (0..1)
    frac_day = (t_cur.hour + t_cur.minute / 60.0 + t_cur.second / 3600.0) / 24.0
    end_angle = frac_day * 360

    # Base circle (gray)
    cv2.circle(base, (cx, cy), radius, (50, 50, 50), -1)

    # Draw the progress arc (semi-transparent overlay)
    arc_img = np.zeros_like(base, dtype=np.uint8)
    cv2.ellipse(
        arc_img,
        (cx, cy), (radius, radius),
        -90,  # Start at the top
        -90, -90 + end_angle,
        (255, 255, 255),
        6,
        cv2.LINE_AA
    )
    alpha = 0.5
    base_f = base.astype(np.float32)
    arc_f = arc_img.astype(np.float32)
    mask_3d = (arc_img > 0)
    out_f = base_f.copy()
    out_f[mask_3d] = (1 - alpha) * base_f[mask_3d] + alpha * arc_f[mask_3d]
    base[:] = out_f.astype(np.uint8)

    # Write the day at the center
    day_str = str(t_cur.day)
    font = cv2.FONT_HERSHEY_SIMPLEX
    (tw, th), _ = cv2.getTextSize(day_str, font, 0.8, 2)
    cv2.putText(base, day_str, (cx - tw // 2, cy + th // 2), font, 0.8, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(base, day_str, (cx - tw // 2, cy + th // 2), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

    # Write the month above the circle
    month_str = t_cur.strftime("%b").upper()
    font_bold = cv2.FONT_HERSHEY_DUPLEX
    (tw2, th2), _ = cv2.getTextSize(month_str, font_bold, 0.5, 2)
    mx = cx - tw2 // 2
    my = cy - radius - 5
    cv2.putText(base, month_str, (mx, my), font_bold, 0.5, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(base, month_str, (mx, my), font_bold, 0.5, (255, 255, 255), 2, cv2.LINE_AA)


###############################################################################
# 4. Generate Animation (Including Accelerated Time When No Typhoon)
###############################################################################
def generate_typhoon_animation(csv_file, map_file, output_file,
                               nw_min_lat, nw_max_lat, nw_min_lon, nw_max_lon,
                               crop_width, crop_height,
                               frames_per_3h, fps,
                               ty_icon_radius,
                               ex_threshold_lat,
                               empty_speedup_factor,
                               static_frames_after_end):
    """
    Generate the typhoon animation video.
    """
    # 1) Load the map
    world_img = load_world_map(map_file)
    world_h, world_w, _ = world_img.shape

    # 2) Parse WP typhoons
    storms = parse_typhoon_data(csv_file, ex_threshold_lat)
    all_times = []
    for sid, track in storms.items():
        for p in track:
            all_times.append(p['time'])
    if not all_times:
        print("No typhoon data available.")
        return
    start_t = min(all_times)
    end_t = max(all_times)
    print("Data coverage:", start_t, "~", end_t)

    # 3) Interpolation based on the original code => big_list[(time, sid, info)] + time_dict
    big_list = []
    for sid, track in storms.items():
        if len(track) < 2:
            # Cannot interpolate with less than 2 points
            for p in track:
                big_list.append((p['time'], sid, p))
            continue
        frames_list = []
        for i in range(len(track) - 1):
            p0 = track[i]
            p1 = track[i + 1]
            # Calculate interpolation within the segment
            d_h = (p1['time'] - p0['time']).total_seconds() / 3600.0
            seg_frames = int(round(d_h / 3 * frames_per_3h))
            seg = []
            # Custom interpolation function (including start and end points)
            if seg_frames < 1:
                seg_frames = 1
            dt_sec = (p1['time'] - p0['time']).total_seconds()
            for fidx in range(seg_frames + 1):
                alpha = fidx / float(seg_frames)
                tt = p0['time'] + timedelta(seconds=alpha * dt_sec)
                lat_i = p0['lat'] + alpha * (p1['lat'] - p0['lat'])
                lon_i = p0['lon'] + alpha * (p1['lon'] - p0['lon'])
                w_i = p0['intensity'] + alpha * (p1['intensity'] - p0['intensity'])
                seg.append({
                    'time': tt,
                    'lat': lat_i,
                    'lon': lon_i,
                    'intensity': w_i,
                    'cat': p0['cat'],
                    'name': p0['name']
                })
            if not frames_list:
                frames_list = seg
            else:
                # Remove duplicate last point from the previous segment
                frames_list += seg[1:]
        # Add to big_list
        for fdata in frames_list:
            big_list.append((fdata['time'], sid, fdata))

    big_list.sort(key=lambda x: x[0])
    # Group by time => time_dict[t] = [(sid, data),...]
    time_dict = OrderedDict()
    for (t, sid, d) in big_list:
        if t not in time_dict:
            time_dict[t] = []
        time_dict[t].append((sid, d))

    sorted_times = list(time_dict.keys())
    print("Number of interpolated time points:", len(sorted_times))

    # 4) Iterate through adjacent time points, accelerate when no typhoon
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (crop_width, crop_height))
    if not out.isOpened():
        print("Failed to create VideoWriter.")
        return

    # Initialize path tracking
    active_typhoon_paths = {}  # key: sid, value: list of {'x', 'y', 'intensity'}
    dissipated_typhoons = []  # list of {'sid': sid, 'path': [...], 'frames_since_dissipation': int, 'faded': bool}

    # Parameters for drawing the time circle
    time_circle_params = (80, crop_height - 80, 35)  # (cx, cy, radius)

    def draw_path_line(base, typhoon, faded=False, opacity=1.0, thickness=1):
        """
        Draw the complete trajectory line of a typhoon.
        """
        path = typhoon['path']
        if len(path) < 2:
            return

        # Create an overlay for handling opacity
        overlay = np.zeros_like(base, dtype=np.uint8)

        for i in range(1, len(path)):
            pt1 = path[i - 1]
            pt2 = path[i]
            color = multi_segment_color(pt1['intensity'])
            cv2.line(overlay, (pt1['x'], pt1['y']), (pt2['x'], pt2['y']), color, thickness, cv2.LINE_AA)

        # Set opacity
        cv2.addWeighted(overlay, opacity, base, 1.0, 0, base)

    def draw_and_write_frame(t_now, active_typhoon_paths, dissipated_typhoons):
        """
        Given the current world time `t_now`:
        1) Crop the map.
        2) Draw trajectory lines.
        3) Draw the time circle.
        4) Draw typhoon icons.
        5) Write the frame.
        """
        # Crop and copy the map
        base = crop_nw_pacific(world_img, nw_min_lat, nw_max_lat, nw_min_lon, nw_max_lon, crop_width, crop_height)

        # Draw trajectory lines
        for typhoon in dissipated_typhoons:
            # Update frame count
            typhoon['frames_since_dissipation'] += 1

            # Check if fade-out should start
            if typhoon['frames_since_dissipation'] == 5 * fps:
                typhoon['faded'] = True

            # Draw the trajectory line
            if typhoon['faded']:
                # Faded trajectory line
                draw_path_line(base, typhoon, faded=True, opacity=0.5, thickness=1)
            else:
                # Full opacity trajectory line
                draw_path_line(base, typhoon, faded=False, opacity=1.0, thickness=1)

        # Draw active typhoons' trajectories
        for sid, path in active_typhoon_paths.items():
            if len(path) < 2:
                continue
            # Draw the trajectory line
            draw_path_line(base, {'path': path}, faded=False, opacity=1.0, thickness=1)

        # Draw the time progress circle
        draw_time_circle(base, t_now, time_circle_params)

        # Draw typhoon icons
        if t_now in time_dict:
            angle_deg = (int((t_now - start_t).total_seconds() / 3600) * 5) % 360
            for (sid, fdata) in time_dict[t_now]:
                lat = fdata['lat']
                lon = fdata['lon']
                w = fdata['intensity']
                cat = fdata['cat']
                name = fdata['name']
                x, y = latlon_to_crop_xy(lat, lon, world_w, world_h, nw_min_lat, nw_max_lat, nw_min_lon, nw_max_lon,
                                         crop_width, crop_height)

                # Record the complete path
                if sid not in active_typhoon_paths:
                    active_typhoon_paths[sid] = []
                active_typhoon_paths[sid].append({'x': x, 'y': y, 'intensity': w})

                # If category is EX, move to dissipated typhoons
                if cat == "EX":
                    dissipated_typhoons.append({
                        'sid': sid,
                        'path': active_typhoon_paths[sid].copy(),
                        'frames_since_dissipation': 0,
                        'faded': False
                    })
                    del active_typhoon_paths[sid]

                # Draw the typhoon icon (draw last to ensure it's on top)
                draw_typhoon_icon(base, x, y, w, cat, angle_deg, name, ty_icon_radius)

        # Write the frame to the video
        out.write(base)

    # Use tqdm to display a progress bar
    total_iterations = len(sorted_times) - 1 if len(sorted_times) > 1 else 1
    with tqdm(total=total_iterations, desc="Generating video frames", unit="frame") as pbar:
        # Iterate through sorted_times
        # Write the first time point
        if sorted_times:
            draw_and_write_frame(sorted_times[0], active_typhoon_paths, dissipated_typhoons)
            pbar.update(1)

        for i in range(len(sorted_times) - 1):
            tA = sorted_times[i]
            tB = sorted_times[i + 1]
            # Time difference in hours
            dt_h = (tB - tA).total_seconds() / 3600.0

            # Check if there is a gap
            if dt_h > 3.1:
                # Gap exists => accelerate by EMPTY_SPEEDUP_FACTOR
                # For example, normal step = dt_base = 3h / FRAMES_PER_3H=0.2h => 12min
                dt_base_h = 3.0 / frames_per_3h  # e.g., 3/15=0.2h => 12min
                real_hours = dt_h
                # Accelerate by EMPTY_SPEEDUP_FACTOR => step= dt_base_h * EMPTY_SPEEDUP_FACTOR
                skip_h = dt_base_h * empty_speedup_factor
                steps = int(math.floor(real_hours / skip_h))
                if steps < 1:
                    steps = 1

                # Generate intermediate times
                for sidx in range(1, steps + 1):
                    alpha = sidx / float(steps)
                    t_now = tA + timedelta(hours=real_hours * alpha)
                    draw_and_write_frame(t_now, active_typhoon_paths, dissipated_typhoons)
                    pbar.update(1)
            else:
                # Normal typhoon interpolation
                draw_and_write_frame(tB, active_typhoon_paths, dissipated_typhoons)
                pbar.update(1)

    # Ensure all dissipated typhoons' trajectories have fully faded out
    max_additional_frames = 0
    for typhoon in dissipated_typhoons:
        frames_remaining = max(0, 5 * fps - typhoon['frames_since_dissipation'])
        if frames_remaining > max_additional_frames:
            max_additional_frames = frames_remaining

    # Generate frames for trajectory fade-out
    for _ in range(max_additional_frames):
        t_now = end_t + timedelta(seconds=_ / fps)
        draw_and_write_frame(t_now, active_typhoon_paths, dissipated_typhoons)
        pbar.update(1)

    # Add static frames after the video ends (no typhoon icons)
    last_frame = crop_nw_pacific(world_img, nw_min_lat, nw_max_lat, nw_min_lon, nw_max_lon, crop_width, crop_height)
    for _ in range(static_frames_after_end):
        out.write(last_frame)
        pbar.update(1)

    # Release the video writer
    out.release()
    print("Video generation complete:", output_file)
