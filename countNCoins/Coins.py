'''
Created on Sep 6, 2016

@author: oliver
'''
import collections
from decimal import Decimal

class Coins(object):
    '''
    classdocs
    '''

    def __init__(self, value, currency):
        '''
        Constructor
        '''
        self.currency = currency
        self.value = int(float(Decimal(value)) * 100)

    def get_coins_dict(self):
        return self.__coinsDict

    def set_coins_dict(self, value):
        self.__coinsDict = value

    def del_coins_dict(self):
        del self.__coinsDict
        
    def getCurrency(self):
        return self.currency
    
    def getValue(self):
        return self.value / 100.    
    
    def setCurrency(self, currency):
        self.currency = currency
        
    def setValue(self, value):
        self.value = int(float(Decimal(value)) * 100)
        
    def setValueCurrency(self, value, currency):
        self.value = int(float(Decimal(value)) * 100)
        self.currency = currency
        
    def coinTypes(self):
        if self.currency is "Euro":
            self.coins = {200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
        elif self.currency is "Dollar":
            self.coins = {100:0, 50:0, 25:0, 10:0, 5:0, 1:0}
        else:
            print "Only Euro and Dollar implemented so far."
            return
        self.coinsDict = collections.OrderedDict(sorted(self.coins.items(), reverse = True))
        return
    
    def subtractCoin(self):
        for coin in self.coinsDict:
            if coin <= self.value:
                self.coinsDict[coin] += 1 
                self.value -= coin       
                return 
            
    def countCoins(self):
        self.coinTypes()
        while self.value > 0:
            self.subtractCoin()
        return sum(self.coinsDict.values())
    
    coinsDict = property(get_coins_dict, set_coins_dict, del_coins_dict, "coinsDict's docstring")
        

        