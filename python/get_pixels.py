# https://pythonhosted.org/sense-hat/api/#get_pixels

from _return import finish

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.get_pixels()

  finish({ "result": result })
except Exception, e:
  finish(e, 1)
