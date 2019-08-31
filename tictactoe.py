import random

ttt = [["-","-","-"],["-","-","-"],["-","-","-"]]
temp = 0
placeX,placeY = 0, 0
randomX,randomY = 0, 0
cpuValues = []
playerValues = []

#player input
def playerMove():
    placeX = int(input("Enter x value : "))
    placeY = int(input("Enter y value : "))
    playerValues.append(placeX)
    playerValues.append(placeY)
    val = "player"
    if(ttt[placeX][placeY] != "-"):
        print("Wrong input")
        playerMove()

#cpu input
def cpuMove():
    randomX = random.randint(0,2)
    randomY = random.randint(0,2)
    cpuValues.append(randomX)
    cpuValues.append(randomY)
    #print("{} and {}".format(randomX,randomY))
    if (ttt[randomX][randomY] != "-"):
        cpuMove()

#display the board
def display():
    for i in ttt:
        print(' | '.join(str(x) for x in i))
        print("----------")

#redraw the board after any change
def redraw(x, y, val):
    if val == "player":
        ttt[x][y] = "X"
    elif val == "cpu":
        ttt[x][y] = "O"

#check if any player has won the game
def check():
    for i in range(0,2):
        #check horizontally
        if ttt[i][0] == ttt[i][1] and ttt[i][0] == ttt[i][2] and ttt[i][0] != "-":
            #gameover
            print("Winner is "+ttt[i][0])
            return 1
        #check vertically
        elif ttt[0][i] == ttt[1][i] and ttt[0][i] == ttt[2][i] and ttt[0][i] != "-":
            #gameover
            print("Winner is "+ttt[0][i])
            return 1
    #check diagonally
    if ttt[0][0] == ttt[1][1] and ttt[0][0] == ttt[2][2] and ttt[0][0] != "-":
        #gameover
        print("Winner is "+ttt[0][0])
        return 1
    elif ttt[0][2] == ttt[1][1] and ttt[0][2] == ttt[2][1] and ttt[0][2] != "-":
        #gameover
        print("Winner is "+ttt[0][2])
        return 1
    return 0

#call all the functions until tamp is set to 1
while temp != 1:
    playerMove()
    redraw(playerValues[-2],playerValues[-1],"player")
    temp = check()
    print(temp)
    cpuMove()
    redraw(cpuValues[-2],cpuValues[-1],"cpu")
    temp = check()
    display()
