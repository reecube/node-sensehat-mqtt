import argparse

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('y', 'yes', 'true', 't', '1'):
        return True
    elif v.lower() in ('n', 'no', 'false', 'f', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
