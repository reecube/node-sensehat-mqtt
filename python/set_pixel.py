# https://pythonhosted.org/sense-hat/api/#set_pixel

import argparse

from _return import finish

parser = argparse.ArgumentParser(description='Sets an individual LED matrix pixel at the specified X-Y coordinate to the specified colour.')
parser.add_argument('x', type=int, choices=xrange(0, 7), metavar='{ x: 0-7 }',
                    help='0 is on the left, 7 on the right.')
parser.add_argument('y', type=int, choices=xrange(0, 7), metavar='{ y: 0-7 }',
                    help='0 is at the top, 7 at the bottom.')
parser.add_argument('r', type=int, choices=xrange(0, 255), metavar='{ r: 0-255 }',
                    help='The Red element of the pixel.')
parser.add_argument('g', type=int, choices=xrange(0, 255), metavar='{ g: 0-255 }',
                    help='The Green element of the pixel.')
parser.add_argument('b', type=int, choices=xrange(0, 255), metavar='{ b: 0-255 }',
                    help='The Blue element of the pixel.')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.set_pixel(args.x, args.y, args.r, args.g, args.b)

  finish({ "result": True })
except Exception, e:
  finish(e, 1)
