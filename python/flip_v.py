# https://pythonhosted.org/sense-hat/api/#flip_v

import argparse

from _str2bool import str2bool
from _return import finish

parser = argparse.ArgumentParser(description='Flips the image on the LED matrix vertically.')
parser.add_argument('redraw', type=str2bool, default=True,
                    help='Whether or not to redraw what is already being displayed on the LED matrix. Defaults to True')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.flip_v(args.redraw)

  # A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue) representing the flipped image.
  finish({ "result": result })
except Exception, e:
  finish(e, 1)
