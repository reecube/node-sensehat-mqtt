# https://pythonhosted.org/sense-hat/api/#clear

import argparse

from _return import finish

parser = argparse.ArgumentParser(description='Sets the entire LED matrix to a single colour, defaults to blank / off.')
parser.add_argument('-r', type=int, choices=xrange(0, 255), metavar='{ 0-255 }',
                    help='The Red element of the pixel.')
parser.add_argument('-g', type=int, choices=xrange(0, 255), metavar='{ 0-255 }',
                    help='The Green element of the pixel.')
parser.add_argument('-b', type=int, choices=xrange(0, 255), metavar='{ 0-255 }',
                    help='The Blue element of the pixel.')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.clear(args.r, args.g, args.b)

  finish({ "result": True })
except Exception, e:
  finish(e, 1)
