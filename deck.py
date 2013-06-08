import collections
#import random

#Deck card storage convention, the top of the deck is the left of the deque
class Deck:
    

    def __init__(self):
        self.createCardStorage()
        #print 'Deck initialized with Zero cards'

    def createCardStorage(self):
        self.__cardStorage__ = collections.deque()

    def addCard(self, card):
        self.__cardStorage__.append(card)
    
    def dealCard(self):
        return self.__cardStorage__.popleft()
    
    def shuffle(self):
        import random
        random.shuffle(self.__cardStorage__)

    def remainingCards(self):
        return len(self.__cardStorage__)

