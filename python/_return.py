import json
import sys

def finish(data, signal=0):
  try:
    print(json.dumps(data))
  except:
    print(str(data))

  sys.exit(signal)
