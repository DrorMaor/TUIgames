import random
import os
import time
import datetime

# this will print the ■ box with the random color
def ColorPrint(code):
    print("\033[" + str(code) + "m■\033[0m", end = ' ')

def main():
    # clear screen first
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
        
    size = 10
    tempSize = input(f"The default matrix is {size}x{size}. Enter a number to change it.\nOtherwise, hit ENTER to start playing ")
    if tempSize.isnumeric():
        size = int(tempSize)
    ColorsDict = {31: 'Red', 32: 'Green', 33: 'Yellow', 34: 'Blue', 35: 'Magenta', 36: 'Cyan', 37: 'White'}
    ColorsList = list(ColorsDict.keys())
    matrix = [[0 for x in range(size)] for y in range(size)]
    blocks = [[0 for x in range(size)] for y in range(size)]
    
    # build the matrix
    for x in range(size):
        for y in range(size):
            matrix[x][y] = random.randint(ColorsList[0], ColorsList[len(ColorsList) - 1])

    # print the color matrix
    for x in range(size):
        for y in range(size):
            ColorPrint(matrix[x][y])
        print()

    # count the "blocks"
    for x in range(size):
        for y in range(size):
            curr = matrix[x][y]
            # N
            if y > 0 and matrix[x][y-1] == curr and blocks[x][y-1] == 0:
                blocks[x][y-1] = 1
                blocks[x][y] = 1
            # S
            if y < size-1 and matrix[x][y+1] == curr and blocks[x][y+1] == 0:
                blocks[x][y+1] = 1
                blocks[x][y] = 1
            # E
            if x < size-1 and matrix[x+1][y] == curr and blocks[x+1][y] == 0:
                blocks[x+1][y] = 1
                blocks[x][y] = 1
            # W
            if x > 0 and matrix[x-1][y] == curr and blocks[x-1][y] == 0:
                blocks[x-1][y] = 1
                blocks[x][y] = 1
            
    matches = 0
    for x in range(size):
        for y in range(size):
            matches += blocks[x][y]

    start_time = time.time()
    guess = input("How many color blocks are there? ")
    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    print (f"It took you {elapsed} seconds")
    
    if int(guess) == matches:
        print ("YOU ARE A GENIUS !!!")
    else:
        print (f"Sorry, there were {matches}")
    # print the color matches
    for x in range(size):
        for y in range(size):
            if blocks[x][y] == 1:
                ColorPrint(matrix[x][y])
            else:
                ColorPrint(30)
        print()

    if input ("Play again? (Y/N) ").lower() == "y":
        main()
    else:
        print ("Good bye")
        
if __name__ == "__main__":
  main()
