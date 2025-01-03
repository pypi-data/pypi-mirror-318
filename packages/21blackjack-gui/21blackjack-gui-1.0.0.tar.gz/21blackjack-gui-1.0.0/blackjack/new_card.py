"""
new_card.py

Creates a new advanced data type that resembles a card
This card is always randomized
"""

# dependencies
import random

class newCard: # initialises the creation of the card
    def __init__(self):
        self.value = random.randint(1, 11)
        self.symbol = self.randSymbol()
        #END __init__

    def randSymbol(self): # randomize a symbol for the card
        random.seed()
        symbol = random.randint(1,4)
        match symbol:
            case 1:
                symbol = "Spades"
            case 2:
                symbol = "Diamonds"
            case 3:
                symbol = "Hearts"
            case 4:
                symbol = "Clubs"
        return symbol
        #END randSymbol
