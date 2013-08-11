class Card:
    def __init__(self, newValue, newSuit):
        self.value = newValue
        self.suit = newSuit
    
    def __str__(self):
        return self.value + ' of ' + self.suit

    def __repr__(self):
        return self.value + ' of ' +self.suit
