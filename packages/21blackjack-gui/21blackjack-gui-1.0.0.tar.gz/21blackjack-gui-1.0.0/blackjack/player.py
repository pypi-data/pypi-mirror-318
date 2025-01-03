"""
player.py

The module that controls the functionality of you, as the player.
Controls the functionality of using a trump, stand or draw a card.
"""

# dependencies
from blackjack.gui import game_page
import blackjack.new_card as nc
import blackjack.game_utils as u
import time

def drawCard(pile, playerDeck): # draws a random card from the pile into your deck
    print("\nYou draw a card...")
    newCard = pile.pop()
    print("You were dealt a " + str(newCard.value) + " " + newCard.symbol)
    playerDeck.append(newCard)
    #END drawCard

def useTrump(trumpVal, pile, playerDeck, playerTDeck): # uses a trump card
    if u.getTrump(trumpVal, playerTDeck): 
        print("\nYou used a trump card!")
        u.useTrump(trumpVal, pile, playerDeck)
        return True
    else:
        return False
    #END useTrump
