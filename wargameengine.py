import collections
import pokercard
import deck
#from player import *
import player 
from pokerdeck import *
from warplayer import *


#def WarGameEngine():
def addPlayers():
    global player1 
    player1 = WarPlayer('Fred')
    print str(player1.getName()) + ' has been added to the game!'
    global player2 
    player2 = WarPlayer('Ralph')
    print str(player2.getName()) + ' has been added to the game!'

# Idle won't take multiple def statements in the same block, find how to make multiple functions work together.
def dealDecksOut():    #Make Deck, Shuffle up and Deal
    startingDeck = PokerDeck()
    
    startingDeck.shuffle()
#    startingDeck.shuffle()   #Maker sure it's good and shuffled

    print 'Dealing the cards'
    cardsInDeck = startingDeck.remainingCards()
    dealingRounds = cardsInDeck/2
    for i in range(dealingRounds):
    
        dealtCard = startingDeck.dealCard()
    #    player1Deck.addCard(dealtCard) 
        player1.playerDeck.addCard(dealtCard)
        dealtCard = startingDeck.dealCard()
        player2.playerDeck.addCard(dealtCard)
    #    player2Deck.addCard(dealtCard) 
    print str(player1)
    print str(player2)
    
def war():
    if player1.playerDeck.remainingCards() < 4 or player2.playerDeck.remainingCards() < 4:
        print 'Someone does not have enought cards for war; return the cards and try again.'
        return 1
    else:
            
        print 'Declair War!'
        player1DownCard = []
        player2DownCard = []
        for i in range(3):
            player1DownCard.append(player1.warPlayerAction())
            player2DownCard.append(player2.warPlayerAction())
        
        player1WarCard = player1.warPlayerAction()
        #print str(player1.getName()) + ' has the ' + str(player1WarCard)
        player2WarCard = player2.warPlayerAction()
        print str(player2.getName()) + ' has the ' + str(player2WarCard) + ' and ' + str(player1.getName()) + ' has the ' + str(player1WarCard)
        
        if player1WarCard.cardValueRank() > player2WarCard.cardValueRank():
            for i in range(3):
                player1.playerDeck.addCard(player1DownCard.pop())
                player1.playerDeck.addCard(player2DownCard.pop())
            player1.playerDeck.addCard(player1WarCard)
            player1.playerDeck.addCard(player2WarCard)
            print str(player1.getName()) + ' wins the cards.'
            return str(player1.getName())
        
        elif player1WarCard.cardValueRank() < player2WarCard.cardValueRank():
            for i in range(3):
                player2.playerDeck.addCard(player1DownCard.pop())
                player2.playerDeck.addCard(player2DownCard.pop())
            player2.playerDeck.addCard(player1WarCard)
            player2.playerDeck.addCard(player2WarCard)
            print str(player2.getName()) + ' wins the cards.'
            return str(player2.getName())
        
        else:
            winner = war()
            if winner == 1:
                for i in range(3):
                    player1.playerDeck.addCard(player1DownCard.pop())
                    player2.playerDeck.addCard(player2DownCard.pop())
                player1.playerDeck.addCard(player1WarCard)
                player2.playerDeck.addCard(player2WarCard)
                print 'Someone does not have enought cards for war; return the cards and try again.'
                return 1                 
            
            elif winner == str(player1.getName()):
                for i in range(3):
                    player1.playerDeck.addCard(player1DownCard.pop())
                    player1.playerDeck.addCard(player2DownCard.pop())
                player1.playerDeck.addCard(player1WarCard)
                player1.playerDeck.addCard(player2WarCard)
                print str(player1.getName()) + ' wins the cards.'
                return str(player1.getName())
            elif winner == str(player2.getName()):
                for i in range(3):
                    player2.playerDeck.addCard(player1DownCard.pop())
                    player2.playerDeck.addCard(player2DownCard.pop())
                player2.playerDeck.addCard(player1WarCard)
                player2.playerDeck.addCard(player2WarCard)
                print str(player2.getName()) + ' wins the cards.'
                return str(player2.getName())
            else:
                print 'Something really weird happened'
                return 1
    
def playRound():

    player1FightCard = player1.warPlayerAction()
#    print str(player1.getName()) + ' has the ' + str(player1FightCard)
    player2FightCard = player2.warPlayerAction()
    print str(player2.getName()) + ' has the ' + str(player2FightCard) + ' and ' + str(player1.getName()) + ' has the ' + str(player1FightCard)
    
    if player1FightCard.cardValueRank() > player2FightCard.cardValueRank():
        player1.playerDeck.addCard(player1FightCard)
        player1.playerDeck.addCard(player2FightCard)
        print str(player1.getName()) + ' wins the cards.'
    elif player1FightCard.cardValueRank() < player2FightCard.cardValueRank():
        player2.playerDeck.addCard(player1FightCard)
        player2.playerDeck.addCard(player2FightCard)
        print str(player2.getName()) + ' wins the cards.'
    else:
        winner = war()
        if winner == 1:
            player1.playerDeck.addCard(player1FightCard)
            player2.playerDeck.addCard(player2FightCard)
        elif winner == str(player1.getName()):
            player1.playerDeck.addCard(player1FightCard)
            player1.playerDeck.addCard(player2FightCard)
        elif winner == str(player2.getName()):
            player2.playerDeck.addCard(player1FightCard)
            player2.playerDeck.addCard(player2FightCard)
             
        """ This is the old way for war
        #player1CardsLeft = player1.playerDeck.remainingCards()
        #player2CardsLeft = player2.playerDeck.remainingCards()
        if player1.playerDeck.remainingCards() < 4 or player2.playerDeck.remainingCards() < 4:
            print 'Someone does not have enought cards for war; return the cards and try again.'
            player1.playerDeck.addCard(player1FightCard)
            player2.playerDeck.addCard(player2FightCard)
        else:
            print 'Declair War!'
            player1DownCard = list()
            player2DownCard = list()
            for i in range(3):
                player1DownCard.append(player1.warPlayerAction())
                player2DownCard.append(player2.warPlayerAction())
            
            player1WarCard = player1.warPlayerAction()
            #print str(player1.getName()) + ' has the ' + str(player1WarCard)
            player2WarCard = player2.warPlayerAction()
            print str(player2.getName()) + ' has the ' + str(player2WarCard) + ' and ' + str(player1.getName()) + ' has the ' + str(player1WarCard)
            
            if player1WarCard.cardValueRank() > player2WarCard.cardValueRank():
                player1.playerDeck.addCard(player1FightCard)
                player1.playerDeck.addCard(player2FightCard)
                for i in range(3):
                    player1.playerDeck.addCard(player1DownCard.pop())
                    player1.playerDeck.addCard(player2DownCard.pop())
                player1.playerDeck.addCard(player1WarCard)
                player1.playerDeck.addCard(player2WarCard)
                print str(player1.getName()) + ' wins the cards.'
            elif player1WarCard.cardValueRank() < player2WarCard.cardValueRank():
                player2.playerDeck.addCard(player1FightCard)
                player2.playerDeck.addCard(player2FightCard)
                for i in range(3):
                    player2.playerDeck.addCard(player1DownCard.pop())
                    player2.playerDeck.addCard(player2DownCard.pop())
                player2.playerDeck.addCard(player1WarCard)
                player2.playerDeck.addCard(player2WarCard)
                print str(player2.getName()) + ' wins the cards.'
            
            else: #still need to code double war and find a cleaner way to deal with this mess :D
                if player1.playerDeck.remainingCards() < 4 or player2.playerDeck.remainingCards() < 4:
                    print 'Someone does not have enough cards for war; return the cards and try again.'
                    player1.playerDeck.addCard(player1FightCard)
                    player2.playerDeck.addCard(player2FightCard)
                    for i in range(3):
                        player1.playerDeck.addCard(player1DownCard.pop())
                        player2.playerDeck.addCard(player2DownCard.pop())
                    player1.playerDeck.addCard(player1WarCard)
                    player2.playerDeck.addCard(player2WarCard)
                        
                else:
                    print 'Double WAR!'
                    for i in range(3):
                        player1DownCard.append(player1.warPlayerAction())
                        player2DownCard.append(player2.warPlayerAction())
                
                    player1War2Card = player1.warPlayerAction()
                    #print str(player1.getName()) + ' has the ' + str(player1War2Card)
                    player2War2Card = player2.warPlayerAction()
                    print str(player2.getName()) + ' has the ' + str(player2War2Card) + ' and ' + str(player1.getName()) + ' has the ' + str(player1War2Card)
                    
                    if player1War2Card.cardValueRank() > player2War2Card.cardValueRank():
                        player1.playerDeck.addCard(player1FightCard)
                        player1.playerDeck.addCard(player2FightCard)
                        for i in range(6):
                            player1.playerDeck.addCard(player1DownCard.pop())
                            player1.playerDeck.addCard(player2DownCard.pop())
                        player1.playerDeck.addCard(player1WarCard)
                        player1.playerDeck.addCard(player2WarCard)
                        player1.playerDeck.addCard(player1War2Card)
                        player1.playerDeck.addCard(player2War2Card)                
                        print str(player1.getName()) + ' wins the cards.'
                    elif player1War2Card.cardValueRank() < player2War2Card.cardValueRank():
                        player2.playerDeck.addCard(player1FightCard)
                        player2.playerDeck.addCard(player2FightCard)
                        for i in range(6):
                            player2.playerDeck.addCard(player1DownCard.pop())
                            player2.playerDeck.addCard(player2DownCard.pop())
                        player2.playerDeck.addCard(player1WarCard)
                        player2.playerDeck.addCard(player2WarCard)
                        player2.playerDeck.addCard(player1War2Card)
                        player2.playerDeck.addCard(player2War2Card)
                        print str(player2.getName()) + ' wins the cards.'
                    else:
                        player1.playerDeck.addCard(player1FightCard)
                        player2.playerDeck.addCard(player2FightCard)
                        for i in range(6):
                            player1.playerDeck.addCard(player1DownCard.pop())
                            player2.playerDeck.addCard(player2DownCard.pop())
                        player1.playerDeck.addCard(player1WarCard)
                        player2.playerDeck.addCard(player2WarCard)
                        player1.playerDeck.addCard(player1War2Card)
                        player2.playerDeck.addCard(player2War2Card)
                        print 'Nobody wins; players get their cards back.'
        """

def main():
    
    addPlayers()
    dealDecksOut()
    
    #player1CardsLeft = player1.playerDeck.remainingCards()
    #player2CardsLeft = player2.playerDeck.remainingCards()
    i = 0 
    while (player1.playerDeck.remainingCards() != 0) and (player2.playerDeck.remainingCards() != 0):
        
        i += 1
        print 'This is round number ' + str(i) + '. ' + str(player1) + ' and ' + str(player2) + '.'
        playRound()
        #if (player1.playerDeck.remainingCards() != 0) and (player2.playerDeck.remainingCards() != 0):
        #    pass
        #else:
        #    break
        if i >5000:
            break
            
    if player1.playerDeck.remainingCards() == 52:
        print str(player1.getName()) + ' has won the game!'
    elif player2.playerDeck.remainingCards() == 52:
        print str(player2.getName()) + ' has won the game!'
    else:
        print 'Something went wrong and nobody has all the cards.'
    
    if player1.playerDeck.remainingCards() == 0:
        print str(player1.getName()) + ' has lost the game.'
    elif player2.playerDeck.remainingCards() == 0:
        print str(player2.getName()) + ' has won the game.'
    else:
        print 'Something went wrong and the looser still has cards.'
        
    #return str(player1), str(player2)
        
if __name__=="__main__":
    main()
    
    