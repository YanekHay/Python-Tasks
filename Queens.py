######################   QUEENS   ######################
## կա շախմատի տախտակ, պետքա ասի որ սյան ու տողի վրա պետքա թագուհին դրվի

#####################    FUNCTIONS
############ Generating an array with 8 digit numbers [0,1,2,3,4,5,6,7,8] without repetition
def getPossibleSets(firstRow,firstCol):
    for a in range(0,9):
        for b in range(0,9):
            if(b!=a):
                for c in range(0,9):
                    if c!=a and c!=b:
                        for d in range(0,9):
                            if d!=a and d!=b and d!=c:
                                for e in range(0,9):
                                    if e!=a and e!=b and e!=c and e!=d:
                                        for f in range(0,9):
                                            if f!=a and f!=b and f!=c and f!=d and f!=e:
                                                for g in range(0,9):
                                                    if g!=a and g!=b and g!=c and g!=d and g!=e and g!=f:
                                                        for h in range(0,9):
                                                            if h!=a and h!=b and h!=c and h!=d and h!=e and h!=f and h!=g:
                                                                res = (f"{a}{b}{c}{d}{e}{f}{g}{h}")
                                                                if int(res[firstRow-1])==firstCol:
                                                                    possibleSets.append(res)


############## Checking if any number does not interfere another number
###### If everything is ok, append the value to the 
def checkOrder(order):
    b = True
    for i in order:
            posX = order.index(i)+1
            posY = int(i) 
            if posY!=0:           
                for j in order:                
                    if j!=i and int(j)!=0:
                        row = order.index(j)+1
                        col = int(j)
                        if  ((row+col == (posX+posY) or posX == row or posY == col or row-col == posX-posY)):
                            b=False
                            break 
                    #print(col,end = "")
            
    if b:
        validOrders.append(order)    

############## A function for printing a chess table with queens on it
def printTable(order):
    print(f"{' ':<3}",end = "")
    for j in range(1,9):
        print(f"{chr(64+j):<3}",end = "")
    for i in range(1,9):
        print()
        print(f"{i:<3}",end = "")
        for j in range(1,9):
            
            print(f"{'Q'+str(i):<3}", end = "") if int(order[i-1]) == j and order.index(str(j))==i-1 else print(f"{0:<3}",end = "")
        
    
 
        
############## A function for printing the order with numbers
def printOrder(order):
    for i in order:
        if i!="0":
            print(f"{chr(int(i)+64)}{order.index(i)+1:<3} ",end="")
    print("\n")    
#### GLOBALS
possibleSets = []  
validOrders = []

############## Getting the first queen's location ---- A1,B2,...,H8       
firstQueen = input("Enter the first queen's location >>> ")
####### Parsing the values
firstQueenRow = int(firstQueen[-1])
firstQueenCol = int(ord(firstQueen[0].upper())-64)

  


##### Using the generator function
                                                              
getPossibleSets(firstQueenRow,firstQueenCol)

for i in possibleSets:    
    checkOrder(i)


q= 0
for i in validOrders:
    if i.count("0")==0:
        q+=1
        print(f"\n\n************ ORDER {q} *************")    
        printOrder(i)
        printTable(i)   
        
        


print(f"\nThere are {q} possible orders")    
