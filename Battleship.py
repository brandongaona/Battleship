"""Advanced Placement Computer Science Principle Create Performance Task"""
"""Miniature Battle Ship"""

print("This is Miniature Battle Ship\n\nThe Rules are Simple:\nThere are 4 ships of different lengths\nYou must guess the rows and columns in which these ships are located\nIf you guess correctly it is called a hit\nAn incorrect guess is called a miss\n")

import random

grid = [
    [" ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "],
    [" 1 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 2 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 3 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 4 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 5 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 6 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
]

def printGrid():
    for row in grid:
        for elem in row:
            print(elem, end='')
        print()

gameGrid = [
    [" ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "],
    [" 1 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 2 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 3 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 4 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 5 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" 6 ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
]

def printGameGrid():
    for row in gameGrid:
        for elem in row:
            print(elem, end='')
        print()

ship1 = 1
ship2 = 2
ship3 = 3
ship4 = 4

direction = random.randint(1, 2)

def enemyShips():
    ship1Row = ship1Column = ship2Row = ship2Column = 0
    ship3Row = ship3Column = ship4Row = ship4Column = 0
    total = []

    if direction == 1:
        rowShip = random.randint(1, 3)
        placer = random.randint(1, 4)
        ship1Row = rowShip
        ship1Column = placer
        for x in range(ship1):
            grid[rowShip][x + placer] = " X "

        rowShip = random.randint(4, 6)
        placer = random.randint(1, 2)
        ship3Row = rowShip
        ship3Column = placer
        for x in range(ship3):
            grid[rowShip][x + placer] = " X "

        columnShip = random.randint(1, 4)
        placer = random.randint(1, 4)
        ship2Row = placer
        ship2Column = columnShip
        for x in range(ship2):
            if grid[x + placer][columnShip] != " X ":
                grid[x + placer][columnShip] = " X "
            elif grid[x + placer][columnShip] == " X ":
                grid[x + placer + 1][columnShip] = " X "

        columnShip = random.randint(5, 9)
        placer = random.randint(1, 2)
        ship4Row = placer
        ship4Column = columnShip
        for x in range(ship4):
            if grid[x + placer][columnShip] != " X ":
                grid[x + placer][columnShip] = " X "

        total.extend([ship1Row, ship1Column, ship3Row, ship3Column, ship2Row, ship2Column, ship4Row, ship4Column])
        return total

    elif direction == 2:
        rowShip = random.randint(1, 3)
        placer = random.randint(1, 3)
        ship2Row = rowShip
        ship2Column = placer
        for x in range(ship2):
            grid[rowShip][x + placer] = " X "

        rowShip = random.randint(4, 6)
        ship4Row = rowShip
        ship4Column = 1
        for x in range(ship4):
            grid[rowShip][x + 1] = " X "

        columnShip = random.randint(1, 4)
        placer = random.randint(1, 5)
        ship1Row = placer
        ship1Column = columnShip
        for x in range(ship1):
            if grid[x + placer][columnShip] != " X ":
                grid[x + placer][columnShip] = " X "
            elif grid[x + placer][columnShip] == " X ":
                grid[x + placer + 1][columnShip] = " X "

        columnShip = random.randint(5, 9)
        placer = random.randint(1, 3)
        ship3Row = placer
        ship3Column = columnShip
        for x in range(ship3):
            if grid[x + placer][columnShip] != " X ":
                grid[x + placer][columnShip] = " X "

        total.extend([ship1Row, ship1Column, ship3Row, ship3Column, ship2Row, ship2Column, ship4Row, ship4Column])
        return total

def getRowGuess(rowGuess):
    while rowGuess.isalpha():
        rowGuess = input("Enter a Numerical Value: ")
    while int(rowGuess) < 1 or int(rowGuess) > 6:
        rowGuess = input("Enter a Row on the Board: ")
        while rowGuess.isalpha():
            rowGuess = input("Enter a Numerical Value: ")
    return int(rowGuess)

def getColumnGuess(columnGuess):
    while columnGuess.isalpha():
        columnGuess = input("Enter a Numerical Value: ")
    while int(columnGuess) < 1 or int(columnGuess) > 9:
        columnGuess = input("Enter a Column on the Board: ")
        while columnGuess.isalpha():
            columnGuess = input("Enter a Numerical Value: ")
    return int(columnGuess)

def getShipGuess(a, b):
    if grid[a][b] == " X ":
        if gameGrid[a][b] == " X ":
            return "You already guessed that!"
        else:
            gameGrid[a][b] = " X "
            return "That's a Hit!"
    else:
        if gameGrid[a][b] == " O ":
            return "You already guessed that!"
        else:
            gameGrid[a][b] = " O "
            return "That's a Miss!"

printGrid()
print()
es = enemyShips()
gamePlay = True
guessCount = 0
missCount = 0
hitCount = 0

while gamePlay:
    rowGuess = input("Guess a Row: ")
    a = getRowGuess(rowGuess)
    print(a, "\n")

    columnGuess = input("Guess a Column: ")
    b = getColumnGuess(columnGuess)
    print(b, "\n")

    c = getShipGuess(a, b)
    print(c, "\n")

    if c == "That's a Hit!":
        hitCount += 1
    elif c == "That's a Miss!":
        missCount += 1

    guessCount += 1
    printGameGrid()

    if hitCount == 10:
        print("You won in", guessCount, "guesses!")
        print("You had", missCount, "misses!")
        if guessCount <= 25:
            print("You had a great game!")
        elif guessCount <= 35:
            print("You had a pretty decent game!")
        else:
            print("You took a lot of guesses, but congrats!")

        playAgain = input("Want to play again? ")
        while not playAgain.isalpha() or playAgain.lower() not in ["yes", "no"]:
            playAgain = input("Must say Yes or No: ")

        if playAgain.lower() == "no":
            gamePlay = False
        elif playAgain.lower() == "yes":
            hitCount = 0
            missCount = 0
            guessCount = 0
            # reset grids and ships
            # reinitialize grid and gameGrid here
            direction = random.randint(1, 2)
            es = enemyShips()
            print()
            printGameGrid()
