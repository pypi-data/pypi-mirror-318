"""
init_page.py

Creates the launch window of the program when initialised.
Called upon launching the program from init.py
"""

# dependencies
from tkinter import *
from blackjack.gui import login_page

def create(): # create main window
    WIDTH = 1000
    HEIGHT = 500
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.config(bg="black")
    main.title("Main Menu")

    menu = Menu(main)
    main.config(menu=menu)

    header = Label(main, text="Blackjack!", font=("Arial", 40), bg="black", fg="white")

    newProfile = Button(main, text="New Profile", font=("Arial", 30), bg="black", fg="white", command=lambda: login_page.enterProfile(main, 0))
    existingProfile = Button(main, text="Login", font=("Arial", 30), bg="black", fg="white", command=lambda: login_page.enterProfile(main, 1))

    header.place(relx=0.5, rely=0.2, anchor=CENTER)
    newProfile.place(relx=0.5, rely=0.4, anchor=CENTER)
    existingProfile.place(relx=0.5, rely=0.6, anchor=CENTER)

    main.mainloop()
    #END create