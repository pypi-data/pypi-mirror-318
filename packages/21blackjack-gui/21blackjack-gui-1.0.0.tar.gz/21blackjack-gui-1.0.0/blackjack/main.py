"""
main.py

The root of the program.
This is called upon launching the program.
"""

# dependencies
from blackjack.gui import game_page
from blackjack.gui import init_page
from blackjack.gui import login_page
from blackjack.gui import menu_page
from blackjack.userstats import dbInit

def init(): # initialises the program and directs flow
    dbInit() # init database
    init_page.create() # login
    userID = login_page.fetchUserID()
    if userID != -1:
        menu_page.create(userID) # main menu
    userID = login_page.fetchUserID()
    if userID != -1:
        game_page.create(userID) # game
    #END init

if __name__ == "__main__":
    init() 
