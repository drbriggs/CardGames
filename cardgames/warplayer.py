from player import *
from deck import *

class WarPlayer(Player):

    def __init__(self, name):
        self.setName(name)
        self.playerDeck = Deck()
        #print "Player initialized"
        
    def playerDeck(self):
        self.playerDeck = Deck()
    
    def warPlayerAction(self):
        return self.playerDeck.dealCard()
        
    def __str__(self):
        return self.getName() + ' has ' + str(self.playerDeck.remainingCards()) + ' cards'