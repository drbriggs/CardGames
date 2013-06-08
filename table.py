########
#Class for basic needs of a poker table
########

import collections
from pot import Pot
#import player
#import pokerplayer

class Table():
    def __init__(self, chairCount):
        players = []
        pot = Pot()
        seats = []
        dealOrder = []
        button = 1
        muck = collections.deque()
        for i in range(chairCount):
            seats.append('open')
            

########

    def findOpenChair(self):
        for i in len(self.seats):
            if self.seats[i] == 'open':
                print 'Seat number ' + (i+1) + ' is open' 
            
    def addPlayer(self,player,chair):
        if self.seats[chair - 1] == 'open':
            self.seats.insert(chair - 1, player)
            self.seats.pop(chair)
        else:
            print 'Chair number ' + chair + ' is not available please choose another chair'
            print 'The available chairs are: ' 
            self.findOpenChair()
        
    def setHandPlayers(self): # Defines the players for any hand, ignoring any empty chairs
        for i in len(self.seats):
            if self.seats[i] != 'open':
                self.players.append(self.seats[i])
            else:
                pass
            
    def setDealOrder(self, buttonStartingLocation): #  Allows for knowing which player to deal to first
        self.button = buttonStartingLocation
        for i in range(len(self.players)):
            if (self.button + i) < len(self.players):
                self.dealOrder.append(self.players[self.button + i])
            elif (self.button + i) >= len(self.players):
                self.dealOrder.append(self.players[i - self.button])
        
    def moveButton(self): # to be done between each hand to rotate the button
        #self.__dealOrder__.rotate(1)
        if self.button + 1 > len(self.players):
            self.button = 1
        else:
            self.button += 1
        self.setDealOrder(self.button)
    
    def muckCards(self,card):  #For use when burning cards or folding hands
        self.muck.append(card)
        
    def deckMuck(self): # Put the muck cards back into the Deck
        return self.muck.popleft()
    
    
    