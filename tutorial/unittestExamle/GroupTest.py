import unittest
from .TestSetMethods import *
from .TestStringMethods import *

class GroupTest(unittest.TestSuite):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestStringMethods('test'));


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(GroupTest().suite())
