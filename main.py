"""
This example will run on Python3.8 and OpenCV4.

****** IMPORTANT *******
There are some assumptions:
  1. The input is the result of yolo sign detection (ex. data/images/panel.jpg)
  2. It only detect single square
  3. The resolution is high enough
  4. All panels are the same size
  5. There is no rotation in image
  6. There is no prespective in image


Usage:
    python3 main.py --source path/to/image
    
    Example:
        python3 main.py --source data/images/panel.jpg

    or use default path:
        python3 main.py

"""

import argparse
import os
import sys
from pathlib import Path

from utils.contour import bit_detecttion
from utils.homography import homography


FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default=ROOT / 'data/images/panel1.jpg', help='file/dir/URL/glob')
    opt = parser.parse_args()
    return opt


def main(opt):
    bit_detecttion(**vars(opt))

    # # To crop the image, uncomment this part.
    # # You need to find the four corners of the the panel manually.
    # # The corners are top-left, top-right, bottom-left, and bottom-right of panel respectively.
    # corners = [[3,5], [79,6], [2,18], [79,19]]
    # homography('data/images/test4.jpeg', corners, save=True, output='data/images/hd4.jpg')

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)

