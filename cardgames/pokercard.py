class PokerCard:
    
    validValues = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    validSuits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']


    def __init__(self, newValue, newSuit):

        if newValue in PokerCard.validValues:
            self.__cardValue__ = newValue
        else:
            raise ValueError(str(newValue) + ' is not a poker card value. Valid values are ' + ",".join(PokerCard.validValues))
    
        if newSuit in PokerCard.validSuits:
            self.__cardSuit__ = newSuit
        else:
            raise ValueError(str(newSuit) + ' is not a poker suit.  Valid values are ' + ",".join(PokerCard.validSuits))

    def cardValueRank(self):
        if self.__cardValue__ == 'Two':
            return 2
        elif self.__cardValue__ == 'Three':
            return 3
        elif self.__cardValue__ == 'Four':
            return 4
        elif self.__cardValue__ == 'Five':
            return 5
        elif self.__cardValue__ == 'Six':
            return 6
        elif self.__cardValue__ == 'Seven':
            return 7
        elif self.__cardValue__ == 'Eight':
            return 8
        elif self.__cardValue__ == 'Nine':
            return 9
        elif self.__cardValue__ == 'Ten':
            return 10
        elif self.__cardValue__ == 'Jack':
            return 11
        elif self.__cardValue__ == 'Queen':
            return 12
        elif self.__cardValue__ == 'King':
            return 13
        elif self.__cardValue__ == 'Ace':
            return 14
        else:
            raise ValueError(str(self.__cardValue__) + ' is not a poker card value. Valid values are ' + ",".join(PokerCard.validValues))
    
    def cardSuitRank(self):
        if self.__cardSuit__ == 'Spades':
            return 1
        elif self.__cardSuit__ == 'Hearts':
            return 2
        elif self.__cardSuit__ == 'Diamonds':
            return 3
        elif self.__cardSuit__ == 'Clubs':
            return 4
        else:
            raise ValueError(str(self.__cardSuit__) + ' is not a poker suit.  Valid values are ' + ",".join(PokerCard.validSuits))

    def __str__(self):
        return self.__cardValue__ + ' of ' + self.__cardSuit__

    def __repr__(self):
        return self.__cardValue__ + ' of ' + self.__cardSuit__
