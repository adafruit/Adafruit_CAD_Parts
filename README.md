# Adafruit_CAD_Parts
Fusion 360 design files for various boards, components and parts

## get-previews.py
This script extracts preview PNGs from F3D files (which are actually just ZIPs.) Invoke it with `python get-previews.py` to extract previews for all products that don't already have them. The script will automatically put the images in the right directories.

By default, the script skips over any product folders that already have a PNG matching the title of the product. This means that if you want to export a custom image from Fusion 360 instead of the default thumbnail (let's say, for product 610 DC Jack), as long as you set the filename to match the product name (`610 DC Jack.png`), the script won't overwrite your custom image. You can, however, override this behavior with the `--force` command line flag - this causes the script to overwrite any existing PNGs with the extracted previews.

*Note: This script is written for Python 3, although a quick test indicates Python 2 might work. YMMV.*