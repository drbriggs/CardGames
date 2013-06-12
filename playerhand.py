import pokercard
import deck


class PlayerHand():
    
    def __init__(self):
        self.__wholeHand__ = []
        self.__upCards__ = []
        self.__downCards__ = []
        
    #def addCard(self, PokerCard):
    #    self.__cardStorage__.extend(PokerCard)

    def addUpCard(self, pokerCard):
        self.__upCards__.extend(pokerCard)
        self.__wholeHand__.extend(pokerCard)
        
    def addDownCard(self, pokerCard):
        self.__downCards__.extend(pokerCard)
        self.__wholeHand__.extend(pokerCard)

    def addCard(self, pokerCard):
        self.addDownCard(pokerCard)
                
    def foldHand(self):
        for i in range(len(self.__wholeHand__)):
            self.__wholeHand__.remove()

    def sortHand(self):
        self.__wholeHand__.sort()

    def showHand(self):
        for i in range(len(self.__wholeHand__)):
            print self.__wholeHand__(i)

    def seeUpCards(self):
        for i in range(len(self.__upCards__)):
            print self.__upCards__(i)
            
    def seeDownCards(self):
        for i in range(len(self.__upCards__)):
            print self.__upCards__(i)
        
    
        
#dealing with up and down cards should probably be dealt with here
