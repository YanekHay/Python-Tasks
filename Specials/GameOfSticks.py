sticks = 10

def getInput(playerName):
    while True:
        res = input((f"{playerName}: Enter a number between 1 and 3 >>> "))
        if res!="" and res.isdigit() and int(res)>=1 and int(res)<=3:
            return int(res)
        else:
            print("********** WRONG INPUT **********")

def pullSticks(count):
    global sticks
    sticks-=count
    print(f"{sticks if sticks>0 else 0} sticks left")

def play(player1,player2):
    while True:
        p1 = getInput(player1)
        pullSticks(p1)
        if sticks<=0:
            print(f"\n{player1} won the game.\n*************** Congratulations ***************")
            return
        p2 = getInput(player2)
        pullSticks(p2)
        if sticks<=0:
            print(f"\n{player2} won the game.\n*************** Congratulations ***************")
            return


play("Player1","Player2")
