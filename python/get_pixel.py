# https://pythonhosted.org/sense-hat/api/#get_pixel

import argparse

from _str2bool import str2bool
from _return import finish

parser = argparse.ArgumentParser(description='Get a single pixel')
parser.add_argument('x', type=int, choices=xrange(0, 7), metavar='{ x: 0-7 }',
                    help='0 is on the left, 7 on the right.')
parser.add_argument('y', type=int, choices=xrange(0, 7), metavar='{ y: 0-7 }',
                    help='0 is at the top, 7 at the bottom.')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.get_pixel(args.x, args.y)

  # Returns a list of [R, G, B] representing the colour of an individual LED matrix pixel at the specified X-Y coordinate.
  finish({ "get_pixel": result })
except Exception, e:
  finish(e, 1)
