'''
Created on Sep 6, 2016

@author: oliver
'''
from countNCoins.Coins import Coins

if __name__ == '__main__':
    
    coinsEuro = Coins(5.99, "Euro")
    print coinsEuro.getValue()      
    print coinsEuro.countCoins()
    print coinsEuro.get_coins_dict().items()

    coinsDollar = Coins(5.99, "Dollar")
    print coinsDollar.getValue()      
    print coinsDollar.countCoins()
    print coinsDollar.get_coins_dict().items()
