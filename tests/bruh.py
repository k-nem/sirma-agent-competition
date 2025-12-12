import unittest
from pathlib import Path
import sys

import os 

mpath = Path(os.path.dirname(os.path.realpath(__file__))).parent
sys.path.append(mpath)

import tinyapp



if __name__ == '__main__':
   #  unittest.main()

   print(Path(tinyapp.jsonPath).exists())
   


w