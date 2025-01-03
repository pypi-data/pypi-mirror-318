"""
game_page.py

Methods that deal with all operations linked to user input for gameplay
"""

#dependencies
from blackjack.game_utils import *
from blackjack.player import *
from blackjack.game import *
from tkinter import *

def getName(trumpVal): # grabs the name of the trump card via its trump value
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

def updateTrumps(playerTDeck, action=None, state=[None]): # update trump card text display
    if state[0] is None:
        state[:] = action
    elif playerTDeck is None:
        for i in range(len(state)):
            state[i].config(text="") # clear text
    else:
        for i in range(len(state)):
            state[i].config(text="") # clear text

        for i in range(len(playerTDeck)):
            state[i].config(text="(" + str(playerTDeck[i].trumpVal) + ")" + " - " + str(playerTDeck[i].name) + " : " + str(playerTDeck[i].desc) + "\n") 
    #END updateTrumps

def updateScores(playerScore, dealerScore, action=None, state=[None]): # update score display
    if state[0] is None:
        state[0] = action
    state[0].config(text="Dealer: " + str(dealerScore) + "/3\n" + "Player: " + str(playerScore) + "/3")

    if playerScore == 3:
        state[0].config(text="You Won!", fg="cyan")
    if dealerScore == 3:
        state[0].config(text="You Lost!", fg="red")
    #END updateScores

def updatePlayerAction(action, trumpVal=None, playerDeck=None, state=[None]): # update player action display
    if state[0] is None:
        state[0] = action
    elif action == 0: # draw
        state[0].config(text="You: Draw")
    elif action == 1: # stand
        state[0].config(text="You: Stand")
    elif action == 2: # trump
        state[0].config(text="You: Used " + getName(trumpVal))
    elif action == -1: # end
        state[0].config(text="You: Had " + str(getTotal(playerDeck)) + "/" + str(updateLimit()))
    #END updatePlayerAction

def updateDealerAction(action, trumpVal=None, enemyDeck=None, state=[None]): # update dealer action display
    if state[0] is None:
        state[0] = action
    elif action == 0: # draw
        state[0].config(text="Dealer: Draw")
    elif action == 1: # stand
        state[0].config(text="Dealer: Stand")
    elif action == 2: # trump
        state[0].config(text="Dealer: Used " + getName(trumpVal))
    elif action == -1: # clear
        state[0].config(text="Dealer: Had " + str(getTotal(enemyDeck)) + "/" + str(updateLimit()))
    #END updateDealerAction

def handleSkip(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, skip, trump, submit): # handle player standing
    draw.destroy()
    skip.destroy()
    trump.destroy()
    submit.destroy()

    updatePlayerAction(1)
    print("You stand...")
    window.after(1000, lambda: nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, True))
    #END handleSkip


def handleDrawCard(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, skip, trump, submit): # handle player drawing a card
    draw.destroy()
    skip.destroy()
    trump.destroy()
    submit.destroy()

    updatePlayerAction(0)
    window.after(1000, lambda: drawCard(pile, playerDeck))
    window.after(1000, lambda: nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, False))
    #END handleDrawCard

def handleTrump(window, entry, pile, playerDeck, userID, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, enemyDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, skip, trump, submit): # handle player using a trump
    valid = p.useTrump(entry.get(), pile, playerDeck, playerTDeck)
    if valid:
        window.after(100, lambda: updateDeck(playerDeck, enemyDeck, enemyDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit))
        window.after(100, lambda: updateTrumps(playerTDeck))
        window.after(100, lambda: updatePlayerAction(2, int(entry.get())))

        window.after(200, lambda: draw.destroy())
        window.after(200, lambda: skip.destroy())
        window.after(200, lambda: entry.destroy())
        window.after(200, lambda: submit.destroy())
        window.after(250, lambda: updatePlayerButtons(window, pile, playerDeck, userID, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, enemyDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit))
    else:
        entry.delete(0, END)
    #END handleTrump

def updatePlayerButtons(main, pile, playerDeck, userID, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit): # initialises player buttons for drawing, using trump or standing
    trump = Entry(main, font=("Arial", 15), bg="black", fg="white", insertbackground="white")
    submit = Button(main, text="Use", font=("Arial", 15), bg="black", fg="white", command= lambda: handleTrump(main, trump, pile, playerDeck, userID, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, stand, trump, submit))

    draw = Button(main, text="Draw", font=("Arial", 25), bg="black", fg="white")
    stand = Button(main, text="Stand", font=("Arial", 25), bg="black", fg="white", command=lambda: handleSkip(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, main, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, stand, trump, submit))
    draw.config(command= lambda: handleDrawCard(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, main, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, stand, trump, submit))


    if getTotal(playerDeck) <= updateLimit():
        draw.place(relx="0.2", rely="0.3", anchor="w")
    stand.place(relx="0.1", rely="0.3", anchor="w")
    trump.place(relx="0.4", rely="0.3", anchor="n")
    submit.place(relx="0.4", rely="0.4", anchor="n")
    #END updatePlayerButtons

def deleteLabels(playerDeckDisplay, enemyDeckDisplay, playerLimit, dealerLimit): # delete text displays
    playerDeckDisplay.destroy()
    enemyDeckDisplay.destroy()
    playerLimit.destroy()
    dealerLimit.destroy()
    #END deleteLabels

def updateDeck(playerDeck, enemyDeck, enemyDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit): # updates the display for both decks
    enemyCards = "(???)  "
    playerCards = ""

    for i in range(1, len(enemyDeck)):
        temp = enemyCards
        enemyCards = temp + "(" + enemyDeck[i].symbol + " | " + str(enemyDeck[i].value) + ")  "
    for j in range(len(playerDeck)):
        temp = playerCards
        playerCards = temp + "(" + playerDeck[j].symbol + " | " + str(playerDeck[j].value) + ")  "

    playerDeckDisplay.config(text=playerCards)
    enemyDeckDisplay.config(text=enemyCards)
    playerLimit.config(text=(str(getTotal(playerDeck)) + "/" + str(updateLimit())))
    dealerLimit.config(text=("? + " + str(getTotal(enemyDeck) - enemyDeck[0].value) + "/" + str(updateLimit())))
    #END updateDeck 

def initDeck(main, playerDeck, enemyDeck): # create deck text displays
    enemyCards = "(???)  "
    playerCards = ""

    for i in range(1, len(enemyDeck)):
        temp = enemyCards
        enemyCards = temp + "(" + enemyDeck[i].symbol + " | " + str(enemyDeck[i].value) + ")  "
    for j in range(len(playerDeck)):
        temp = playerCards
        playerCards = temp + "(" + playerDeck[j].symbol + " | " + str(playerDeck[j].value) + ")  "

    dealerDeckDisplay = Label(main, text=enemyCards, font=("Arial", 20), bg="black", fg="white", wraplength=1100)
    dealerLimit = Label(main, text=("? + " + str(getTotal(enemyDeck) - enemyDeck[0].value) + "/" + str(updateLimit())), font=("Arial", 20), bg="black", fg="white")
    playerDeckDisplay = Label(main, text=playerCards, font=("Arial", 20), bg="black", fg="white", wraplength=1100)
    playerLimit = Label(main, text=(str(getTotal(playerDeck)) + "/" + str(updateLimit())), font=("Arial", 20), bg="black", fg="white")
    
    dealerDeckDisplay.place(relx="0.75", rely="0.3", anchor="n")
    dealerLimit.place(relx="0.75", rely="0.15", anchor="n")
    playerDeckDisplay.place(relx="0.75", rely="0.9", anchor="s")
    playerLimit.place(relx="0.75", rely="0.75", anchor="s")

    return dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit
    #END initDeck

def create(userID): # create the main window for the game
    WIDTH = 1200
    HEIGHT = 700
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.title("Game")
    main.config(bg="black")

    dealerTitle = Label(main, text="Dealer", font=("Arial", 20), bg="black", fg="white")
    playerTitle = Label(main, text="Player", font=("Arial", 20), bg="black", fg="white")

    playerAction = Label(main, text="You: ", font=("Arial", 20), bg="black", fg="white")
    dealerAction = Label(main, text="Dealer: ", font=("Arial", 20), bg="black", fg="white")

    trumpLabel1 = Label(main, text="Your Trump Slot", font=("Arial", 15), bg="black", fg="white")
    trumpLabel2 = Label(main, text="Your Trump Slot", font=("Arial", 15), bg="black", fg="white")
    trumpLabel3 = Label(main, text="Your Trump Slot", font=("Arial", 15), bg="black", fg="white")
    scoreLabel = Label(main, text="You: ", font=("Arial", 20), bg="black", fg="white")

    dealerTitle.place(relx="0.75", rely="0.1", anchor="n")
    playerTitle.place(relx="0.75", rely="0.7", anchor="s")

    dealerAction.place(relx="0.1", rely="0.4", anchor="n")
    playerAction.place(relx="0.1", rely="0.5", anchor="s")

    scoreLabel.place(relx="0.1", rely="0.9", anchor="w")
    trumpLabel1.place(relx="0.35", rely="0.65", anchor="s")
    trumpLabel2.place(relx="0.35", rely="0.75", anchor="s")
    trumpLabel3.place(relx="0.35", rely="0.85", anchor="s")

    trumpLabels = [trumpLabel1, trumpLabel2, trumpLabel3]

    main.after(100, lambda: updateDealerAction(dealerAction))
    main.after(100, lambda: updatePlayerAction(playerAction))
    main.after(100, lambda: updateScores(0, 0, scoreLabel))
    main.after(100, lambda: updateTrumps(None, trumpLabels))
    main.after(1000, lambda: init(userID, 0, 0, main)) # schedule init to run after creating main game window
    main.mainloop()
    #END create

