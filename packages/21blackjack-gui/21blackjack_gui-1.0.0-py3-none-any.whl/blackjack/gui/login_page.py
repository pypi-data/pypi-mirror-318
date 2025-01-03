"""
login_page.py

Methods that deal with all operations linked to profiles
"""

#dependencies
from tkinter import *
from blackjack.userstats import newProfile, login as existingProfile

def fetchUserID(val=None, userID=[-1]): # retrieves user ID
    if val is None:
        return userID[0]
    else:
        userID[0] = val
    #END fetchUserID

def getUserID(main, login, usernameEntry, passwordEntry, invalid, type): # type = 0 = new profile / type = 1 = existing profile
    # fetch user id if exists
    if type == 0:
        userID = newProfile(usernameEntry.get(), passwordEntry.get())
    elif type == 1:
        userID = existingProfile(usernameEntry.get(), passwordEntry.get())
    if userID is None:
            usernameEntry.delete(0, END)
            passwordEntry.delete(0, END)
            invalid.place(relx=0.7, rely=0.85, anchor="w")
    else:
        login.destroy()
        main.destroy()
        fetchUserID(userID) # update to users ID
    #END getUserID

def enterProfile(main, type): # init creation/functionality of profile page
    WIDTH = 500
    HEIGHT = 400
    login = Toplevel(main)
    login.geometry(str(WIDTH) + "x" + str(HEIGHT))
    login.config(bg="black")
    login.title = "Create Profile"

    createProfilePage(main, login, type)

    main.withdraw() # hide main window

    def close():
        main.deiconify()  
        login.destroy()   
    login.protocol("WM_DELETE_WINDOW", close)

    login.mainloop()
    #END enterProfile

def createProfilePage(main, login, type): # create login page
    if type == 0:
        title = "Create Profile"
    elif type == 1:
        title = "Login"

    header = Label(login, text=title, font=("Arial", 20), bg="black", fg="white")
    username = Label(login, text="Username: ", font=("Arial", 15), bg="black", fg="white")
    password = Label(login, text="Password: ", font=("Arial", 15), bg="black", fg="white")
    invalid = Label(login, text="Invalid!", font=("Arial", 20), bg="black", fg="red")

    usernameEntry = Entry(login, font=("Arial", 15), bg="black", fg="white", insertbackground="white")
    passwordEntry = Entry(login, font=("Arial", 15), bg="black", fg="white", insertbackground="white")

    submit = Button(login, text=title, font=("Arial", 20), bg="black", fg="white", command=lambda: getUserID(main, login, usernameEntry, passwordEntry, invalid, type))

    submit.place(relx=0.5, rely=0.9, anchor="s")
    header.place(relx=0.5, rely=0.2, anchor=CENTER)
    username.place(relx=0.2, rely=0.4, anchor="w")
    password.place(relx=0.2, rely=0.6, anchor="w")
    usernameEntry.place(relx=0.45, rely=0.4, anchor="w")
    passwordEntry.place(relx=0.45, rely=0.6, anchor="w")
    #END createProfilePage