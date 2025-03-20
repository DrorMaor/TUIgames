import random
import os
import time
from datetime import datetime

ColorsDict = {31: 'Red', 32: 'Green', 33: 'Yellow', 34: 'Blue', 35: 'Magenta', 36: 'Cyan', 37: 'White'}
ColorsList = list(ColorsDict.keys())
OrigMatrixSize = 10
MinMatrixSize = 5

class SessionSummary:
    def __init__(self, StartTime, EndTime, games):
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.games = games
    def __repr__(self):
        return f"SessionSummary({repr(self.StartTime)}, {repr(self.EndTime)}, {repr(self.game)})"
    
class GameSummary:
    def __init__(self, MatrixSize, guess, matches, elapsed):
        self.MatrixSize = MatrixSize
        self.guess = guess
        self.matches = matches
        self.elapsed = elapsed
    def __repr__(self):
        return f"GameSummary({repr(self.MatrixSize)}, {repr(self.guess)}, {repr(self.matches)}, {repr(self.elapsed)})"

sessionSummary = SessionSummary(datetime.now(), None, [])

def ColorPrint(code):
    # this will print the ■ box with the random color
    print("\033[" + str(code) + "m■\033[0m", end = ' ')

def GetGuess():
    while True:
        guess = input("How many color blocks are there? ")
        if guess.isnumeric() and int(guess) >= 0:
            return int(guess)
        else:
            print ("Please enter a non-negative integer")    

def GetYesNo(level):
    while True:
        yn = input(f"Continue with {level} level? (y/n) ").lower()
        if yn == "y" or yn == "n":
            return yn
        else:
            print ("Please enter either Y or N")

def ShowSessionSummary(s):
    os.system('clear')
    StartTime = s.StartTime.strftime("%m/%d/%Y %H:%M:%S")
    EndTime = s.EndTime.strftime("%H:%M:%S")
    print (f"Your session started at {StartTime} and ended at {EndTime}")
    games = "games" if len(s.games) > 1 else "game"
    print (f"You played {len(s.games)} {games}\n")
    counter = 1
    for g in s.games:
        print (f"-- Game #{counter} --")
        print (f"Matrix size: {g.MatrixSize}x{g.MatrixSize}")
        print (f"Your guess: {g.guess}")
        print (f"Actual matches: {g.matches}")
        print (f"Seconds elapsed: {g.elapsed}")
        print ()
        counter += 1
    
def PlayGame(MatrixSize, GameCounter):
    # clear screen first
    os.system('clear')

    # build the matrix
    matrix = [[0 for x in range(MatrixSize)] for y in range(MatrixSize)]
    blocks = [[0 for x in range(MatrixSize)] for y in range(MatrixSize)]   
    for x in range(MatrixSize):
        for y in range(MatrixSize):
            matrix[x][y] = random.randint(ColorsList[0], ColorsList[len(ColorsList) - 1])

    # print the color matrix
    for x in range(MatrixSize):
        for y in range(MatrixSize):
            ColorPrint(matrix[x][y])
        print()

    # count the "blocks"
    for x in range(MatrixSize):
        for y in range(MatrixSize):
            curr = matrix[x][y]
            # N
            if y > 0 and matrix[x][y-1] == curr and blocks[x][y-1] == 0:
                blocks[x][y-1] = 1
                blocks[x][y] = 1
            # S
            if y < MatrixSize-1 and matrix[x][y+1] == curr and blocks[x][y+1] == 0:
                blocks[x][y+1] = 1
                blocks[x][y] = 1
            # E
            if x < MatrixSize-1 and matrix[x+1][y] == curr and blocks[x+1][y] == 0:
                blocks[x+1][y] = 1
                blocks[x][y] = 1
            # W
            if x > 0 and matrix[x-1][y] == curr and blocks[x-1][y] == 0:
                blocks[x-1][y] = 1
                blocks[x][y] = 1
            
    matches = 0
    for x in range(MatrixSize):
        for y in range(MatrixSize):
            matches += blocks[x][y]

    start_time = time.time()
    print (f"This is game #{GameCounter} with a {MatrixSize}x{MatrixSize} matrix", end='')
    if MatrixSize == MinMatrixSize:
        print (" (your last chance!)")
    else:
        print()

    guess = GetGuess()
    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    print (f"It took you {elapsed} seconds")

    RetVal = 0
    if int(guess) == matches:
        print ("YOU ARE A GENIUS !!!")
        RetVal = MatrixSize + 1
    else:
        print (f"Sorry, there were {matches}")
        RetVal = MatrixSize - 1

    sessionSummary.games.append(GameSummary(MatrixSize, guess, matches, elapsed))
    
    # print the color matches
    for x in range(MatrixSize):
        for y in range(MatrixSize):
            if blocks[x][y] == 1:
                ColorPrint(matrix[x][y])
            else:
                print('  ', end='')
        print()
    
    return RetVal

def main():
    global OrigMatrixSize
    GameCounter = 1
    NewMatrixSize = PlayGame(OrigMatrixSize, GameCounter)
    while NewMatrixSize >= MinMatrixSize:
        level = "a harder" if NewMatrixSize > OrigMatrixSize else "an easier"
        cont = GetYesNo(level)
        if cont == "y":
            OrigMatrixSize = NewMatrixSize
            GameCounter +=1
            NewMatrixSize = PlayGame(NewMatrixSize, GameCounter)
        else:
            print ("Good Bye")
            NewMatrixSize = 1

    sessionSummary.EndTime = datetime.now()
    ShowSessionSummary(sessionSummary)
        
if __name__ == "__main__":
    main()
