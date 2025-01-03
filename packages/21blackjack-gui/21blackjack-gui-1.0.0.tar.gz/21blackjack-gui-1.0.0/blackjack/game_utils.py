"""
game_utils.py

Important game utilities used by both the player and dealer.
"""

# dependencies
import blackjack.new_card as nc
import blackjack.new_trump as nt

def getTotal(deck): # calculates the value sum of cards of the given deck
    sum = 0 
    for i in range(len(deck)):
        sum += deck[i].value
    return sum
    #END getTotal

def updateLimit(newLimit=None, limit=[21]): # updates the card limit from default 21
    if newLimit is None:
         return limit[0]
    else:
        limit[0] = newLimit
        return limit[0]
    #END updateLimit
    
def dupeTrump(deck): # inserts a random trump card in the given deck, avoiding placing in a card thats already within the deck 
    if len(deck) < 3:
        genNewTrump = False
        while not genNewTrump:
            newTrump = nt.newTrumpCard()
            if not any(newTrump.trumpVal == card.trumpVal for card in deck):
                deck.append(newTrump)
                return True
    #END dupeTrump
                
def getTrump(trumpVal, Tdeck): # runs a linear search on the deck to see if it contains the selected trump card or not
    for i in range(len(Tdeck)):
        if int(trumpVal) == Tdeck[i].trumpVal:
            Tdeck.pop(i)
            return True
    return False
    #END getTrump
                
def useTrump(trumpVal, pile=None, deck=None): # calls the method linked to the trump card
    match int(trumpVal):
        case 0:
            trump27()
        case 1:
            trump17()
        case 2:
            trumpRefresh(pile, deck)
        case 3:
            trumpDiscard(pile, deck)
    #END useTrump

def trump27(): # sets card limit to 27
    updateLimit(27)
    print("The card limit has increased to 27!")
    #END trump27

def trump17(): # sets card limit to 17
    updateLimit(17)
    print("The card limit has decreased to 17!")
    #END trump17

def trumpRefresh(pile, deck): # returns a new deck with two random cards from the pile
    newDeck = [pile.pop(), pile.pop()]
    deck[:] = newDeck
    print("Hand discarded, two cards from pile drawn.")
    #END trumpRefresh

def trumpDiscard(pile, deck): # discards the last card drawn
    last = len(deck)-1
    if last >= 2:
        card = deck.pop()
        pile.append(card)
        print("Last card discarded.")
    #END trumpDiscard

   