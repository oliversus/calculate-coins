'''
Created on Sep 7, 2016

@author: oliver
'''
import unittest
from countNCoins.Coins import Coins


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCountCoins(self):
        testCoins = Coins(6.23, "Dollar")
        nCoins = testCoins.countCoins()
        expected = 11
        self.assertEqual(nCoins, expected, "Error in countCoins(): given {}, expected {}.".format(nCoins, expected))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCountCoins']
    unittest.main()