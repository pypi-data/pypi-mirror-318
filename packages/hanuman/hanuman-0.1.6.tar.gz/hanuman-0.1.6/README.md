# Hanuman

Hanuman is a Python tool designed to generate animated videos of typhoon seasons. It processes typhoon data from a CSV file and overlays the trajectories on a world map, creating visually engaging animations that depict the paths and intensities of typhoons over time.

## Features

- **Visualize Typhoon Trajectories**: Overlay typhoon paths on an equirectangular world map.
- **Dynamic Animation**: Generate smooth animations showing the progression of typhoons.
- **Categorization**: Categorize typhoons based on wind speeds, with distinct visual markers.
- **Customizable Parameters**: Adjust map cropping, frame rates, icon sizes, and more.
- **Command-Line Interface**: Easy-to-use CLI for generating animations with custom configurations.

## Installation

Ensure you have Python 3.6 or higher installed. You can install Hanuman directly from PyPI using `pip`:

```bash
pip install hanuman
```

Alternatively, if you prefer to install from source, clone the repository and install the package:

```bash
git clone https://github.com/yourusername/Hanuman.git
cd Hanuman
pip install .
```

# Usage

Hanuman provides a command-line interface to generate typhoon animation videos. Below is a basic example of how to use the tool.

## Basic Command

```bash
hanuman --csv typhoon202411.csv --map world_map.png --output typhoon_season_a13.mp4
```

And the detailed command-line arguments is below:

```bash
hanuman \
    --csv typhoon202411.csv \
    --map world_map.png \
    --output typhoon_season_a13.mp4 \
    --nw_min_lat 0.0 \
    --nw_max_lat 45.0 \
    --nw_min_lon 100.0 \
    --nw_max_lon 180.0 \
    --crop_width 1280 \
    --crop_height 720 \
    --frames_per_3h 15 \
    --fps 30 \
    --ty_icon_radius 24 \
    --ex_threshold_lat 22.0 \
    --empty_speedup_factor 25 \
    --static_frames_after_end 300
```

### Arguments Description

- `--csv`: (Required) Path to the typhoon data CSV file.
- `--map`: (Required) Path to the world map image file (e.g., PNG).
- `--output`: (Optional) Name of the output video file. Default is `typhoon_season_a13.mp4`.
- `--nw_min_lat`: (Optional) NW Pacific minimum latitude. Default is 0.0.
- `--nw_max_lat`: (Optional) NW Pacific maximum latitude. Default is 45.0.
- `--nw_min_lon`: (Optional) NW Pacific minimum longitude. Default is 100.0.
- `--nw_max_lon`: (Optional) NW Pacific maximum longitude. Default is 180.0.
- `--crop_width`: (Optional) Output canvas width in pixels. Default is 1280.
- `--crop_height`: (Optional) Output canvas height in pixels. Default is 720.
- `--frames_per_3h`: (Optional) Frames per 3-hour interpolation interval. Default is 15.
- `--fps`: (Optional) Video frame rate. Default is 30.
- `--ty_icon_radius`: (Optional) Radius of the typhoon icon in pixels. Default is 24.
- `--ex_threshold_lat`: (Optional) Latitude threshold to change category to EX. Default is 22.0.
- `--empty_speedup_factor`: (Optional) Speedup factor when no typhoon is present. Default is 25.
- `--static_frames_after_end`: (Optional) Number of static frames after the video ends. Default is 300.

### Example

Assuming you have a CSV file named `typhoon202411.csv` and a world map image `world_map.png`, you can generate a video as follows:

```
hanuman --csv typhoon202411.csv --map world_map.png --output typhoon_season_a13.mp4
```

An MP4 file will then be generated using the 2024 Northwest Pacific typhoon season as an example. The final video size is approximately 200 MB and will conclude with a complete path still frame, making it convenient for users to continue editing.

<div style="text-align: center;">
<img src="https://ice.frostsky.com/2025/01/01/35303b016defa5531415f98e62328deb.png"> <br> 
<div> <p><small style="color: gray">2024 Typhoon Season Animation <sub>by hanuman</sub></small></p> </div>
</div> 

## Dependencies

Hanuman relies on the following Python packages:

- OpenCV (`opencv-python`)
- NumPy
- tqdm

These dependencies are automatically installed when you install `Hanuman` via pip.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgements

Hanuman was created by CZHanoi in memory of a friend of Hinnamnor. Special thanks to the contributors and the open-source community for their invaluable tools and libraries.