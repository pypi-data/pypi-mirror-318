"""
userstats.py

Controls user profiles.
"""

# dependencies
import sqlite3 as sq
import os

dbPath = os.path.join(os.path.dirname(__file__), 'user.db')

def dbInit():

    connectDatabase = sq.connect(dbPath)
    database = connectDatabase.cursor()

    try:
        database.execute('''
            CREATE TABLE IF NOT EXISTS users
            (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                games INTEGER DEFAULT 0,
                games_won INTEGER DEFAULT 0,
                games_lost INTEGER DEFAULT 0
            )
        ''')
        print("Table creation attempt finished")
    except sq.DatabaseError as e:
        print("Error during table creation")

    connectDatabase.commit()
    connectDatabase.close()

def newProfile(username, password): # insert a new profile into the users table
    connectDatabase = sq.connect(dbPath)
    database = connectDatabase.cursor()

    database.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    userID = database.fetchone()
    if userID is not None:
        print("This username already exists!")
        connectDatabase.close()
    elif username == "" or password == "":
        print("Please enter a username/password!")
        connectDatabase.close()
    else:
        print("New profile created!")
        database.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connectDatabase.commit()

        database.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        userID = database.fetchone()
        connectDatabase.close()
        return userID[0]
    #END newProfile

def login(username, password): # login to an existing profile inside the users table
    connectDatabase = sq.connect(dbPath)
    database = connectDatabase.cursor()

    database.execute("SELECT user_id FROM users WHERE username = ? AND password = ?", (username, password))
    userID = database.fetchone()
    if userID is None:
        print("That username or password is incorrect!")
        connectDatabase.close()
    else:
        print("Logged in!")
        connectDatabase.close()
        return userID[0]
    #END login

def updateStats(userID, stats): # update games, win, loss stats accordingly
    connectDatabase = sq.connect(dbPath)
    database = connectDatabase.cursor()

    database.execute("UPDATE users SET games = games + 1 WHERE user_id = ?", [userID])
    match stats:
        case 0: # win
            database.execute("UPDATE users SET games_won = games_won + 1 WHERE user_id = ?", [userID])
            connectDatabase.commit()
        case 1: # lose
            database.execute("UPDATE users SET games_lost = games_lost + 1 WHERE user_id = ?", [userID])
            connectDatabase.commit()
    connectDatabase.close()
    #END updateStats
    

def getStats(userID): # prints the users overall stats
    connectDatabase = sq.connect(dbPath)
    database = connectDatabase.cursor()

    database.execute("SELECT games, games_won, games_lost FROM users WHERE user_id = ?", [userID])
    stats = database.fetchone()
    connectDatabase.close()
    return stats
    #END viewStats
