'''
Created on Sep 7, 2016

@author: oliver
'''
import unittest
from countNCoins.Coins import Coins


class coinsTest(unittest.TestCase):


    def setUp(self):
        # initialize coins object
        self.coins = Coins(1.11, "Euro")
 
    def tearDown(self):
        # destroy object after use
        self.coins = None

    def testCountCoinsDollar(self):
        self.coins.setValueCurrency(6.23, "Dollar")   
        given = self.coins.countCoins()
        expected = 11   
        self.assertEqual(given, expected, "Error in countCoins(): given {}, expected {}.".format(given, expected))
        
        self.coins.setValueCurrency(6.33, "Dollar")   
        given = self.coins.countCoins()
        expected = 11
        self.assertEqual(given, expected, "Error in countCoins(): given {}, expected {}.".format(given, expected))
        
        self.coins.setValueCurrency(7.99, "Dollar")   
        given = self.coins.countCoins()
        expected = 15
        self.assertEqual(given, expected, "Error in countCoins(): given {}, expected {}.".format(given, expected))

    def testCountCoinsEuro(self):
        self.coins.setValueCurrency(6.23, "Euro")
        given = self.coins.countCoins()
        expected = 6
        self.assertEqual(given, expected, "Error in countCoins(): given {}, expected {}.".format(given, expected))
        
        self.coins.setValueCurrency(6.33, "Euro")
        given = self.coins.countCoins()
        expected = 7
        self.assertEqual(given, expected, "Error in countCoins(): given {}, expected {}.".format(given, expected))
        
        self.coins.setValueCurrency(7.99, "Euro")
        given = self.coins.countCoins()
        expected = 10
        self.assertEqual(given, expected, "Error in countCoins(): given {}, expected {}.".format(given, expected))
        
if __name__ == "__main__":
    # run the tests with finer level of control
    # create test suite that runs all of the tests above
    suite = unittest.TestLoader().loadTestsFromTestCase(coinsTest)    
    unittest.TextTestRunner(verbosity=2).run(suite)





