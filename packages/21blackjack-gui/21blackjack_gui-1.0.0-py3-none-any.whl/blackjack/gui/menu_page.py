"""
menu_page.py

Methods that deal with all operations linked to the main menu
"""

#dependencies
from tkinter import *
from blackjack.userstats import getStats
from blackjack.gui import login_page

def game(main): # launch the game window
    main.destroy()
    #END game

def createRules(main): # create the window to display the rules
    WIDTH = 1000
    HEIGHT = 600
    rules = Toplevel(main)
    rules.geometry(str(WIDTH) + "x" + str(HEIGHT))
    rules.title("Rules")
    rules.config(bg="black")

    header = Label(rules, text="Rules", font=("Arial", 30), bg="black", fg="white")
    allRules = Label(rules, wraplength=WIDTH-10, text="1. You and the dealer will always start off with 2 random cards in your deck, where your first card will always be hidden to your opponent(same goes for dealer).\n2. You must either draw a card, or pass - If you choose to draw a card, you will be given a random card from 1 to 11 that will be added to your deck. If you pass, you will skip to the dealers turn.\n3. The goal of the game is to draw cards until you get a sum up to 21 - However, going above this limit limits your turn to a pass and a win for the dealer, and vice versa.\n4. If both parties pass, then this result in a showdown, where the 'judge' compares the total points of both decks, and the player closest to 21 is the winner!\n5. However, it should be noted that if you get the same points as the dealer, this will not result in a draw, rather a loss for you.\n6. First to 3 wins is declared as the winner.", font=("Arial", 20), bg="black", fg="white")

    def close():
        main.deiconify()  
        rules.destroy()   
    rules.protocol("WM_DELETE_WINDOW", close)

    main.withdraw()

    header.pack()
    allRules.pack()

    rules.mainloop()

    #END rules

def createStats(main, userID): # create window to display user stats
    WIDTH = 900
    HEIGHT = 500
    stats = Toplevel(main)
    stats.geometry(str(WIDTH) + "x" + str(HEIGHT))
    stats.config(bg="black")
    stats.title = "Statistics"

    playerStats = getStats(userID)
    header = Label(stats, text="Satistics", font=("Arial", 30), bg="black", fg="white")
    games = Label(stats, text="Games Played : " + str(playerStats[0]), font=("Arial", 25), bg="black", fg="white")
    gamesWon = Label(stats, text="Games Won : " + str(playerStats[1]), font=("Arial", 25), bg="black", fg="white")
    gamesLost = Label(stats, text="Games Lost : " + str(playerStats[2]), font=("Arial", 25), bg="black", fg="white")

    def close(): # handle closing window
        main.deiconify()  
        stats.destroy()   
    stats.protocol("WM_DELETE_WINDOW", close)

    main.withdraw()

    header.place(relx=0.5, rely=0.1, anchor='n')
    games.place(relx=0.5, rely=0.4, anchor=CENTER)
    gamesWon.place(relx=0.5, rely=0.6, anchor=CENTER)
    gamesLost.place(relx=0.5, rely=0.8, anchor=CENTER)
    stats.mainloop()
    #END createStats

def create(userID): # create main window
    WIDTH = 1000
    HEIGHT = 500
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.config(bg="black")
    main.title("Main Menu")

    menu = Menu(main)
    main.config(menu=menu)

    header = Label(main, text="Main Menu", font=("Arial", 40), bg="black", fg="white")

    play = Button(main, text="Play Against Dealer", font=("Arial", 30), bg="black", fg="white", command=lambda: game(main))
    stats = Button(main, text="View Statistics", font=("Arial", 30), bg="black", fg="white", command=lambda: createStats(main, userID))
    rules = Button(main, text="Rules", font=("Arial", 30), bg="black", fg="white", command=lambda: createRules(main))

    header.place(relx=0.5, rely=0.1, anchor='n')
    play.place(relx=0.5, rely=0.4, anchor=CENTER)
    stats.place(relx=0.5, rely=0.6, anchor=CENTER)
    rules.place(relx=0.5, rely=0.8, anchor=CENTER)

    def close(): # handle closing window
        login_page.fetchUserID(-1)
        main.destroy()
    main.protocol("WM_DELETE_WINDOW", close)

    main.mainloop()
    #END create