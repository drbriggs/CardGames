from pokercard import PokerCard
from deck import Deck


class PokerDeck(Deck):
    
    def __init__(self):
        self.createCardStorage()
        #for each poker value and suit create a card and add it to the deck
        for v in PokerCard.validValues:
            for s in PokerCard.validSuits:
                self.addCard(PokerCard(v, s))
        print 'Deck initialized with ' + str(self.remainingCards()) + ' cards'
