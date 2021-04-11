# https://pythonhosted.org/sense-hat/api/#get_pixels

import argparse

from _return import finish

parser = argparse.ArgumentParser(description='Get all 8x8 pixels')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.get_pixels()

  finish({ "result": result })
except Exception, e:
  finish(e, 1)
