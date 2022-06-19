# list compression
# mylist = [i for i in range(15) if i%2 ==0]
# print(mylist)

### Task No. 110
# mylist = []
# while True:
#     inp = int(input("Enter a number >>> "))
#     if(inp==0):
#         break
#     mylist.append(inp)
# mylist.sort()
# print(mylist)
# print(mylist)

### Task No. 111
# mylist = []
# while True:
#     inp = int(input("Enter a number >>> "))
#     if(inp==0):
#         break
#     mylist.append(inp)

# mylist = mylist[::-1]
# for i in mylist:
#     print (i)

### Task No. 112   
# mylist = []
# while True:
#     inp = int(input("Enter a number >>> "))
#     if(inp==0):
#         if(len(mylist)<4):
#             print("ERROR: Input more than 4 elements")
#             quit()
#         break
#     mylist.append(inp)

# mylist.sort()

# print(mylist)
# n = int(input("n = "))
# while n*2>=len(mylist):
#     n = int(input("Enter smaller n\nn = "))
# for i in range(n+1):
#     del mylist[0]
#     print(mylist)
#     del mylist[len(mylist)-1]
    
### Task No. 113

# rightOrder = ["first","second","third","fourth","fifth","sixth","seventh"]

# userInput = []
# while True:
#     inp = input("Enter an order >>> ")
#     if(inp==""):
#         break
#     if(inp.lower() not in rightOrder):
#         print("Wrong input")
#         continue
#     if(inp.lower() not in userInput):
#         userInput.append(inp)

# print(userInput)

### Task No. 114
# userInput = []

# negatives = []
# zeros = []
# positives = []
# while True:
#     inp = input("Enter an order >>> ")
#     if(inp==""):
#         break
#     userInput.append(int(inp))

# for i in userInput:
#     if i<0:
#         negatives.append(i)
#     elif i==0:
#         zeros.append(i)
#     elif i>0:
#         positives.append(i)
        
# result = negatives + zeros + positives

# print(result)

### Task No. 115
# import math
# divisors = []
## Getting input
# while True:
#     num = int(input("Enter a number >>> "))
#     if(num>0):
#         break
#     else:
#         print("Wrong Input")
#         continue
### Getting divisors
# for i in range(1,round(math.sqrt(num))+1):
#     temp = round(num/i)      
#     if(num%i==0):
#         divisors.append(i)
#         if(temp!=i):
#             divisors.append(temp)

# divisors.sort()
# print(divisors)   

### Task No. 116
# import math

# perfects = []
# for num in range(2,100):
#     divisors = []    
#     for i in range(1,round(math.sqrt(num))+1):   
#         temp = round(num/i)
#         if(num%i==0):
#             divisors.append(i)
#             if(temp!=num and temp!=i):
#                 divisors.append(temp)
#     print(i,divisors)            
#     #print(num,divisors)
#     s = 0
#     for divisor in divisors:
#         s+=divisor
#     if(num == s):
#         perfects.append(num)    

# print(perfects)

### Task No. 117
# inp = input("Enter some text >>> ")
# while inp=="":
#     inp = input("Enter some text >>> ")
# words = inp.split(" ")
# print (words)

### Task No. 118
# text = input("Enter some text >>> ")
# punctuation = "!@#$%^&*()_+-=`[]{};':,./<>?"
# for i in punctuation:
#     if i in text:
        
#         text = text.replace(i,"")
        
# words = text.lower().split(" ")
# if words==words[::-1]:
#     print("Palindrome")
# else:
#     print("Not Panlindrome")

### Task No. 119
# values = []
# avg = 0
# while True:
#     inp = input("Enter a number >>> ")
#     if inp=="":
#         break
#     values.append(int(inp))
#     avg+=int(inp)
# avg = avg/len(values)
# print (avg)


# less = []
# avgs = []
# values.sort()

# for i in values:
#     if i>avg:
#         break
#     elif i<avg:
#         less.append(i)
#     else:
#         avgs.append(i)      
    

# print("Values less than average value >>> ",less,"\nAverage values entered >>> ", avgs if len(avgs)>0 else "[none]")        

### Task No. 120
# wordArr = []
# while True:
#     word = input("Enter a word >>> ")
#     if word=="":
#         break
#     wordArr.append(word)

# if len(wordArr)==1:
#     print(wordArr[0])
# else:
#     for i in range(0,len(wordArr)-1):
#         print(wordArr[i],end = " and " if i == len(wordArr)-2 else ", ")
#     print(f"{wordArr[-1]}")

### Task No. 121
# import random

# ticket = []
# for i in range(6):
#     rnum = random.randint(1,49)
#     while rnum in ticket:
#         rnum = random.randint(1,49)
#     ticket.append(rnum)
    

# print(ticket)
# ticket.sort()
# print("Ascending  >>>",ticket)
# ticket.sort(reverse=True)
# print("Descending >>>",ticket)

### Task No. 122
# punctuation = "!@#$%^&*()_+-=`[]{};':,./<>?"
# vowels = "auieo"

# text = input("Enter some text >>> ")
# #Cleaning text
# for i in punctuation:
#     if i in text:
#         text = text.replace(i,"")

# #Task part        
# words = text.split(" ")
# pigLat = []
# for word in words:
#     if word[0] in vowels:
#         pigLat.append(f"{word}way")
#     else:
#         sliceInd = 0
#         for i in range(len(word)):
#             if word[i] in vowels:
#                 sliceInd = i
#                 break
#         print (word[:sliceInd])
#         pigLat.append(f"{word[sliceInd:len(word)]}{word[0:sliceInd]}ay")


# print(pigLat)

### Task No. 123
# punctuation = "!@#$%^&*()_+-=`[]{};':,./\|~<>?"
# vowels = "auieo"

# text = input("Enter some text >>> ")

# words = text.split(" ")
# pigLat = []
# for word in words:
#     w= word[0:len(word)-1]
#     tx=""
#     if w[0].lower() in vowels:
#         tx= f"{w.capitalize()}way{word[-1]} "
#     else:
#         sliceInd = 0
#         for i in range(len(word)):
#             if w[i] in vowels:
#                 sliceInd = i
#                 break
#         tx = f"{w[sliceInd:len(w)]}{w[0:sliceInd].lower()}ay{word[-1]} "
        
#     pigLat.append(tx.capitalize() if word[0].isupper() else tx)

# finText = "".join(pigLat)
# print(finText)
### Task No. 124
# xArr=[]
# yArr=[]
# while True:
#     x = input("x = ")
#     if(x==""):
#         break
#     y= input("y = ")
#     print(x,y)
#     xArr.append(float(x))
#     yArr.append(float(y))

# n = len(xArr)
# print(xArr,"\n",yArr)
# avgX = 0
# avgY = 0
# up = 0
# bottom = 0
# for i in range(n):
#     avgX+=xArr[i]
#     avgY+=yArr[i]
#     up += xArr[i]*yArr[i]
#     bottom += xArr[i]*xArr[i]
# up = up-(avgX*avgY/n)
# bottom = bottom-(avgX*avgX/n)

# avgX /= n    
# avgY /= n

# print (up,bottom,avgX,avgY)
# m = up/bottom  
# b= avgY-m*avgX

# print(f"y = {m:.2f}x + {b:.2f}")

### Task No. 125
# ("spades", "hearts", "diamonds", "clubs")
# Ten, Jack, Queen, King, Ace
# import random 

# suits = ("s", "h", "d", "c")
# values = (2,3,4,5,6,7,8,9,"T","J","Q","K","A")

# # Generate Card Deck
# deck = []
# for i in values:
#     for j in suits:
#         deck.append(str(i) + j)

# print(deck,len(deck))
# #Shuffling
# for i in range(0,len(deck)):
#     r= random.randint(0,len(deck)-1)
#     temp = deck[i]
#     deck[i] = deck[r]
#     deck[r] = temp

# print("*************Shuffled*************\n",deck)


### Task No. 126
# import random 

# suits = ("s", "h", "d", "c")
# values = (2,3,4,5,6,7,8,9,"T","J","Q","K","A")

# # Generate Card Deck
# deck = []
# hands = []
# for i in values:
#     for j in suits:
#         deck.append(str(i) + j)


# #Shuffling
# for i in range(0,len(deck)):
#     r= random.randint(0,len(deck)-1)
#     temp = deck[i]
#     deck[i] = deck[r]
#     deck[r] = temp
# print("*************Shuffled*************\n",deck)
# for i in range(0,4):
#     hand = []
#     for j in range(0,5):
#         r = random.randint(0,len(deck))
#         hand.append(deck[r])
#         del deck[r]
#     hands.append(hand)    
# print(deck,"\n*********************************\n",hands)   


### Task No. 127
# import random
# lst  = []
# for i in range(0,random.randint(5,30)):
#     lst.append(random.randint(100,1000))
# sortTest = lst[:]
# sortTest.sort()    
# print("Given list is sorted by ascending order" if lst==sortTest else \
#       "Given list is sorted by descending order" if lst==sortTest[::-1] else "list is not sorted" )
# print(lst)
### Task No. 128
# import random
# items = []
# for i in range(0,random.randint(5,30)):
#     items.append(random.randint(100,1000))
# min = float(input("Enter a minimum value >>> "))
# max = float(input("Enter a maximum value >>> "))
# q = 0
# for i in items:
#     if i>min and i<max:
#         q+=1
# print(items,"\nThe count of items is >>> ",q)
### Task No. 129
# inp = input("Enter an expression >>> ")
# operators = "+-*/=()^%><"
# #Remove spaces
# inp = inp.replace(" ","")
# tokenArr = []
# token = ""
# print(inp)
# lastOpInd = 0
# for i in inp:    
#     if i in operators:
#         if token!="":
#             tokenArr.append(token)
#         tokenArr.append(i)
#         lastOpInd = i
#         token = ""
#         continue        
#     token = f"{token}{i}"    
# tokenArr.append(token)   
# print(tokenArr)

### Task No. 130
## V 1.0
# expression = ["-","1","+","5","*","+","(","-","5","+","2",")"]
# operators = "/*-+!@#$%^&(_<>?|"
# unary = "+-"
# # print("Enter the expression below(black to finish)")
# # while True:
# #     inp = input("Enter a token >>> ")
# #     if (inp==""):
# #         break
# #     expression.append(inp)    
# print("".join(expression))
# if(expression[0] in unary):
#     expression[0] = "u" + expression[0]
    
# for i in range(1,len(expression)):
#     if (expression[i-1] in operators) and (expression[i] in unary):
#         expression[i] = "u" + expression[i]
# print(expression)



### Task No. 131
# inp = input("Enter an expression >>> ")
# operators = "+-*/=(^%><?|"
# unary = "+-"
# #Remove spaces
# inp = inp.replace(" ","")
# inFixExpression = []
# token = ""
# print(inp)

# ## Tokenizing a string 
# for i in inp:    
#     if i in operators:
#         if token!="":
#             inFixExpression.append(token)
#         inFixExpression.append(i)
#         token = ""
#         continue        
#     token = f"{token}{i}"    
# inFixExpression.append(token)   
# print(inFixExpression)

# ## Finding unar operators
# print("".join(inFixExpression))
# if(inFixExpression[0] in unary):
#     inFixExpression[0] = "u" + inFixExpression[0]
    
# for i in range(1,len(inFixExpression)):
#     if (inFixExpression[i-1] in operators) and (inFixExpression[i] in unary):
#         inFixExpression[i] = "u" + inFixExpression[i]
# print(inFixExpression)

# ## Creating postFix expression
# postFixexpression = []
# numbers = []
# opers = []
# for i in inFixExpression:
#     if i in operators or i in ["u+","u-"]:
#         opers.append(i)
#     else:
#         numbers.append(i)

# postFixexpression = numbers + opers
# print(postFixexpression)

# V 2.0

inp = input("Enter an expression >>> ")
operators = "+-*/=(^%><?|"
unary = "+-"
#Remove spaces
inp = inp.replace(" ","")
inFixExpression = []
token = ""
print(inp)

## Tokenizing a string 
for i in inp:    
    if i in operators:
        if token!="":
            inFixExpression.append(token)
        inFixExpression.append(i)
        token = ""
        continue        
    token = f"{token}{i}"    
inFixExpression.append(token)   
print(inFixExpression)

## Finding unar operators
print("".join(inFixExpression))
if(inFixExpression[0] in unary):
    inFixExpression[0] = "u" + inFixExpression[0]
    
for i in range(1,len(inFixExpression)):
    if (inFixExpression[i-1] in operators) and (inFixExpression[i] in unary):
        inFixExpression[i] = "u" + inFixExpression[i]
print(inFixExpression)

###
postFixOperators = []
postFixExpression = []

for i in range(len(inFixExpression)):
    print(postFixOperators)
    if inFixExpression[i].isdigit():
        postFixExpression.append(inFixExpression[i])
    else:
        while len(postFixOperators)!=0 and postFixOperators[-1]!="(" and inFixExpression[i-1]<postFixOperators[-2]:
            postFixExpression.append(postFixOperators[-1])
            del postFixOperators[-1]
        if inFixExpression[i]=="(":
            postFixOperators.append(inFixExpression[i])
        elif inFixExpression[i]==")":
            while postFixOperators[-1]!="(":
                postFixExpression.append(postFixOperators[-1])
                del postFixOperators[-1]
            while postFixOperators!=[] :
                postFixExpression.append[postFixOperators[-1]]
                del postFixOperators[-1]           

print(postFixExpression)    


### Task No. 132
#----------------------------------------------------
### Task No. 133
# larger = [1,2,3,4]
# smaller = [1,2]

# for i in range(len(larger)):
#     for j in range(len(smaller)):
        
### Task No. 134
### Task No. 135

#######################################  123, 131, ...

####### Slides
### Task 13.1
# lst  = [1,5,3,52,(1,5,3,"bar",'a'),12,0,94]

# q=0
# for i in lst:
#     print(type(i))
#     if type(i) is tuple:
#         break
#     q+=1

# print(q)     
### Task 13.2
# tup = (5,1,2,"add","what","sun",1.2,195)
# tup = tup[::-1]
# print(tup)
### Task 13.3
# tup = (5,1,2,"add","what","sun",1.2,195)
# print(len(tup))
### Task 13.4
# tup = (5,1,2,"add","what","sun",1.2,195)
# text = "".join(str(tup))
# print (text) 
### Task 13.5
# tup = (5,1,2,1.2,195)
# s = 0
# for i in tup:
#     s+=i
# print(s)
### Task 13.6
# tup = (5,1,2,"add","what","sun",1.2,195)
# for i in tup:
#     if type(i) is str :
#         print(i)

### Task 14.1
# lst = [1,5,1,32,23,8200,8,1]
# s = 0
# for i in lst:
#     s+=i
# print(s)
### Task 14.2
# lst = [1,5,1,32,23,10,8,1]
# p=1
# for i in lst:
#     p*=i
# print(p)
### Task 14.3
# lst = [1,5,1,32,23,10,8,1]
# lst.sort()
# print(lst[-1])
### Task 14.4
# list1 = [1,5,1,32,23,10,8,1]
# list2 = [99,56,4,98,316,2,89,12]

# b= False
# for i in list1:
#     if i in list2:
#         b=True        
#         break

# print("Lists have common members" if b else "Lists have nothing in common")


