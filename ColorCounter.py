import random
import os
import time
import datetime

# this will print the ■ box with the random color
def ColorPrint(code):
    print("\033[" + str(code) + "m■\033[0m", end = ' ')

def main():
    # clear screen first
    os.system('cls')
    size = 10
    ColorsDict = {31: 'Red', 32: 'Green', 33: 'Yellow', 34: 'Blue', 35: 'Magenta', 36: 'Cyan', 37: 'White'}
    ColorsList = list(ColorsDict.keys())
    matrix = [[0 for x in range(size)] for y in range(size)]
    AllCurr = [[0 for x in range(size)] for y in range(size)]

    for x in range(size):
        for y in range(size):
            matrix[x][y] = random.randint(ColorsList[0], ColorsList[len(ColorsList) - 1])

    # print the color matrix
    for x in range(size):
        for y in range(size):
            ColorPrint(matrix[x][y])
        print()

    # count the "dupes"
    for x in range(size):
        for y in range(size):
            curr = matrix[x][y]
            # N
            if y > 0 and matrix[x][y-1] == curr and AllCurr[x][y-1] == 0:
                AllCurr[x][y-1] = 1
                AllCurr[x][y] = 1
            # S
            if y < size-1 and matrix[x][y+1] == curr and AllCurr[x][y+1] == 0:
                AllCurr[x][y+1] = 1
                AllCurr[x][y] = 1
            # E
            if x < size-1 and matrix[x+1][y] == curr and AllCurr[x+1][y] == 0:
                AllCurr[x+1][y] = 1
                AllCurr[x][y] = 1
            # W
            if x > 0 and matrix[x-1][y] == curr and AllCurr[x-1][y] == 0:
                AllCurr[x-1][y] = 1
                AllCurr[x][y] = 1
            
    matches = 0
    for x in range(size):
        for y in range(size):
            matches += AllCurr[x][y]

    start_time = time.time()
    guess = input("How many matches are there? ")
    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    print (f"It took you {elapsed} seconds")
    with open("results.txt", 'a') as file:
        now = datetime.datetime.now()
        # Time of Game	elapsed	guess	actual
        text = "\n" + now.strftime("%m/%d/%Y %H:%M:%S") + "\t" + str(elapsed) + "\t" + str(guess) + "\t" + str(matches)
        file.write(text)
    
    if int(guess) == matches:
        print ("YOU ARE CORRECT !!!!")
    else:
        print (f"Sorry, there were {matches}")
    # print the color matches
    for x in range(size):
        for y in range(size):
            if AllCurr[x][y] == 1:
                ColorPrint(matrix[x][y])
            else:
                ColorPrint(30)
        print()

    if input("Play again? (Y/N) ").lower() == "y":
        main()
    else:
        if input("Would you like to see your results? (Y/N) ").lower() == "y":
            with open("results.txt", 'r') as file:
                lines = file.read()
                print (lines)
                print()
        print ("Good bye")
        
if __name__ == "__main__":
  main()

