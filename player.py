########
#Class for basic needs of any card game player
########

class Player():
    
    def __init__(self):
        #print 'Player initialized'
        self.__playerName__ = 'unknown'
        
    def setName(self, name):
        self.__playerName__ = name
        
    def getName(self):
        return self.__playerName__
    
    def __str__(self):
        return self.__playerName__
        
#    def playerAction(self):
#        return action
        