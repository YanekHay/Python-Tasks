##############################
# կնոպկով հեռախոսի խնդիրը 
buttons = {
    '1':"",
    '2':"ABC",
    '3':"DEF",
    '4':"GHI",
    '5':"JKL",
    '6':"MNO",
    '7':"PQRS",
    '8':"TUV",
    '9':"WXYZ",
    '0':" ",
    '*':"*+",
    "#":"#"    
}


inp = input("Enter the digits >>> ")
depth = len(inp)

counters = [0 for i in range(0,depth)]

def loopRecursion(level):
    global counters
    if level == depth:
        generateVariant()
    else:
        for counter in range(len(buttons[inp[level]])):
            counters[level] = counter
            loopRecursion(level+1)

def generateVariant():
    global inp,counters
    variant = ""
    i=0
    for level in counters:        
        variant += buttons[inp[i]][level]
        i+=1
    print(variant)
            
    
loopRecursion(0)