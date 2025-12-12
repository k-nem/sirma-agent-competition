import unittest
from pathlib import Path

from .. import app

class testClass:

    def testDataExists(self):
       assertTrue(Path(app.jsonPath).exists())


 if __name__ == '__main__':
    unittest.main()


