# https://pythonhosted.org/sense-hat/api/#set_rotation

import argparse

from _str2bool import str2bool
from _return import finish

parser = argparse.ArgumentParser(description='If you are using the Pi upside down or sideways you can use this function to correct the orientation of the image being shown.')
parser.add_argument('r', type=int, choices={0, 90, 180, 270},
                    help='The angle to rotate the LED matrix though. 0 is with the Raspberry Pi HDMI port facing downwards.')
parser.add_argument('redraw', type=str2bool, nargs='?', default=True,
                    help='Whether or not to redraw what is already being displayed on the LED matrix. Defaults to True')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  sense.set_rotation(args.r, args.redraw)

  finish({ "result": True })
except Exception, e:
  finish(e, 1)
