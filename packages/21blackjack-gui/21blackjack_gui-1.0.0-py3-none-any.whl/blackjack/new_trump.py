"""
new_trump.py

Creates a new advanced data type that resembles a trump card
The type of trump card is always randomized
"""

# dependencies
import random

class newTrumpCard: # initialises the creation of a new trump card
    def __init__(self):
        self.trumpVal = self.randTrump()
        self.name = self.getName(self.trumpVal)
        self.desc = self.getDesc(self.trumpVal)
        #END __init__

    def randTrump(self): # randomises a trump value, the type of trump card this will be
        random.seed()
        trumpVal = random.randint(0,3)
        match trumpVal:
            case 0:
                trumpVal = 0
            case 1:
                trumpVal = 1
            case 2:
                trumpVal = 2
            case 3:
                trumpVal = 3
        return trumpVal
        #END randTrump
    
    def getName(self, trumpVal): # grabs the name of the new trump card via its trump value
        match trumpVal:
            case 0:
                return "27"
            case 1:
                return "17"
            case 2:
                return "Refresh"
            case 3:
                return "Discard"
        #END getName
            
    def getDesc(self, trumpVal): # grabs the description of the new trump card via its trump value
        match trumpVal:
            case 0:
                return "Increases the cap from 21 to 27"
            case 1:
                return "Decreases the cap from 21 to 17"
            case 2:
               return "Discards hand, draws 2 random cards and ends turn"
            case 3:
               return "Discards the last drawn card"
        #END getDesc
