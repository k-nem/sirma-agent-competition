import unittest
from pathlib import Path
import sys
import os 

pkgPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if pkgPath not in sys.path: sys.path.append(pkgPath)

from core import app

class testClass(unittest.TestCase):

    def testDataExists(self):
      self.assertTrue(Path(app.jsonPath).exists(),
                      'Data not found')
      
    def testDataLoads(self):
      self.assertIsInstance(app.readJson(app.jsonPath), dict,
                      'The data is not a valid JSON')

if __name__ == '__main__':
   unittest.main()