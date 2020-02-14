target = __import__("../main.py")

import unittest

class Test(unittest.TestCase):
    def linkTest(self):
        r = target.askLink();
        return true

if __name__ == '__main__':
    unittest.main()
