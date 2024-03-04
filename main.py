#!/bin/python3

import os,sys
from pathlib import Path
root = Path(os.path.dirname( __file__ ))

'''
#import another module from anywhere
modPath = root/"module"
sys.path.append(modPath)
'''
def runProg():
    print(__name__)
    print(sys.argv)    
    print(sys.path)

if __name__ == "__main__":
    runProg()
    pass
