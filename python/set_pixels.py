# https://pythonhosted.org/sense-hat/api/#set_pixels

import argparse

from _img_array import imgArray
from _return import finish

parser = argparse.ArgumentParser(description='Updates the entire LED matrix based on a 64 length list of pixel values.')
parser.add_argument('pixel_list', type=imgArray,
                    help='A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue). Each R-G-B element must be an integer between 0 and 255.')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  sense.set_pixels(args.pixel_list)

  finish({ "result": True })
except Exception, e:
  finish(e, 1)
