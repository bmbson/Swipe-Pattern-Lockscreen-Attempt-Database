"""
Program: Pattern Unlock Attempt Memorizer
Use: Remembers attempted swipe pattern combinations.
Made By: BMBSON
Version: 0.1
"""

import sqlite3

#Creates patterns.db if it doesnt exist
def createDb():
    con = sqlite3.connect("patterns.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS patterns (id integer primary key, pattern INTEGER NOT NULL UNIQUE)''')
    con.commit()
    con.close()

#Used to put the pattern into DB
def patternIntoDb(patternChoice):
    con = sqlite3.connect("patterns.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO patterns (pattern) values (?)", [patternChoice])
    except:
        print("Duplicate entry. Try again\n")
        
    con.commit()
    con.close()

def listDbContents():
    con = sqlite3.connect("patterns.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patterns")
    print(cur.fetchall())
    con.close()


#Gives info about program and patterns
def info():
    #Gives info about common patterns.
    print()
    print("Patterns that are entered are saved inside a database. Enter the pattern before inputting it into the phone to see if you've already tried it before.")
    print("Some facts: \n - 44% of all patterns start in the top left corner. \n - 77% of all patterns use a corner.\n - average among of nodes is 5. \n - patterns often move from left to right and from top to bottom. \n - Patterns are between 2 and 9 nodes.\n")

#Checks user input.
def patternEntryControl():
    LOCKSCREENPATTERN = "\n(1)(2)(3)\n(4)(5)(6)\n(7)(8)(9)\n"
    print(LOCKSCREENPATTERN)
    patternChoice = None

    while True:
        print("Enter a combination between 4 and 9 nodes (example: 146257).\n")
        patternChoice = input()

        if patternChoice.isnumeric() == False:
            print("Your input contains non-number characters.\nTry again.\n")
        elif len(patternChoice) < 2:
            print("\nYour entry is less than 4 characters long\nTry again.\n")
        elif len(patternChoice) > 9:
            print("\nYour entry is more than 9 characters long\nTry again.\n")
        else:
            break
    
    print("%s has been entered" %patternChoice)
    return patternChoice

createDb()
print("Pattern Unlock Attempt Memorizer\n")

while True:
    print("""P Enter Pattern 
I Info
X Exit
L List DB
""")

    menuChoice = input()

    if menuChoice == "i" or menuChoice == "I":
        info()

    elif menuChoice == "p" or menuChoice == "P":
        patternIntoDb(patternEntryControl())

    elif menuChoice == "x" or menuChoice == "X":
        exit()

    elif menuChoice == "l" or menuChoice =="L":
        listDbContents()

    else:
        print("\nThe command %s is not recognized" %menuChoice)
    
