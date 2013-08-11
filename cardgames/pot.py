########
#Class to keep track of the money on the table
########
class Pot():

    

    def __init__(self):
        __potAmount__ = 0

    def addMoney(self, money):
        __potAmount__ = self.__potAmount__ + money

    def checkPot(self):
        return self.__potAmount__

    def payWinner(self):
        self.__winnings__ = self.__potAmount__
        __potAmount__ = 0
        return self.__winnings__

    def playersInPot(self):
        #find a way to check if a player has put money in the pot and is active and return those players' names