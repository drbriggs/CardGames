class PlayerStack():

    __dollarAmount__ = 0

    def __init__(self, buyIn):
        __dollarAmount__ = buyIn

    def addMoney(self, money):
        self.__dollarAmount__ = self.__dollarAmount__ + money

    def checkStack(self):
        return self.__dollarAmount__

    def makeBet(self, bet):
        if bet >= self.__dollarAmount__:
            self.allIn()
        else:
            self.__dollarAmount__ = self.__dollarAmount__ - bet
        
    def allIn(self):
        bet = self.__dollarAmount__
        __dollarAmount__ = 0
        return bet

