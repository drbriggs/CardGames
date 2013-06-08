from player import Player
#from pokercard import PokerCard
from playerhand import PlayerHand
from playerstack import PlayerStack

class PokerPlayer(Player):

    def __init__(self, name, buyIn):
        self.setName(name)
        hand = PlayerHand()
        stack = PlayerStack(buyIn)
        self.setStatus(True)
        
    def setStatus(self, inHand):
        self.status = inHand
        
    def getStatus(self):
        return self.status
        
            
    
    #need to figure out how to deal with getting cards, having up cards and down cards
    #being able to see down cards and show up cards to other players
    #fix in player hand and make easily accessible here
        