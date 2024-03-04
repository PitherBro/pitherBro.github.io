#!/bin/python3

import os,sys
from pathlib import Path
root = Path(os.path.dirname( __file__ ))

'''
#import another module from anywhere
modPath = root/"module"
sys.path.append(modPath)
'''

if __name__ == "__main__":
    print("welcom to the Home page")
    pass
