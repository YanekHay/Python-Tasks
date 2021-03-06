### Task No. 110 Sorted Order
# mylist = []
# while True:
#     inp = int(input("Enter a number >>> "))
#     if(inp==0):
#         break
#     mylist.append(inp)
# mylist.sort()
# print(mylist)
# print(mylist)

### Task No. 111 Reverse Order
# mylist = []
# while True:
#     inp = int(input("Enter a number >>> "))
#     if(inp==0):
#         break
#     mylist.append(inp)

# mylist = mylist[::-1]
# for i in mylist:
#     print (i)

### Task No. 112 Remove Outliers
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
    
### Task No. 113 Avoiding Duplicates

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

### Task No. 114 Negatives,Zeros and Positives
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

### Task No. 115 List of Proper Divisors
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

### Task No. 116 Perfect Numbers
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

### Task No. 117 Only theWords
# inp = input("Enter some text >>> ")
# while inp=="":
#     inp = input("Enter some text >>> ")
# words = inp.split(" ")
# print (words)

### Task No. 118 Word byWord Palindromes
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

### Task No. 119 Below and Above Average
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

### Task No. 120 Formatting a List
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

### Task No. 121 Random Lottery Numbers
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

### Task No. 122 Pig Latin
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


### Task No. 123 Pig Latin Improved
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


### Task No. 124 Line of Best Fit
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

### Task No. 125 Shuffling a Deck of Cards
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


### Task No. 126 Dealing Hands of Cards
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


### Task No. 127 Is a List already in Sorted Order?
# import random
# lst  = []
# for i in range(0,random.randint(5,30)):
#     lst.append(random.randint(100,1000))
# sortTest = lst[:]
# sortTest.sort()    
# print("Given list is sorted by ascending order" if lst==sortTest else \
#       "Given list is sorted by descending order" if lst==sortTest[::-1] else "list is not sorted" )
# print(lst)
### Task No. 128 Count the Elements
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
### Task No. 129 Tokenizing a String
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

### Task No. 130 Unary and Binary Operators
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



### Task No. 131 Infix to Postfix
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

# ###

# postFixOperators = []
# postFixExpression = []

# for i in range(len(inFixExpression)):
#     print(postFixOperators)
#     if inFixExpression[i].isdigit():
#         postFixExpression.append(inFixExpression[i])
#     else:
#         while len(postFixOperators)!=0 and postFixOperators[-1]!="(" and inFixExpression[i-1]<postFixOperators[-2]:
#             postFixExpression.append(postFixOperators[-1])
#             del postFixOperators[-1]
#         if inFixExpression[i]=="(":
#             postFixOperators.append(inFixExpression[i])
#         elif inFixExpression[i]==")":
#             while postFixOperators[-1]!="(":
#                 postFixExpression.append(postFixOperators[-1])
#                 del postFixOperators[-1]
#             while postFixOperators!=[] :
#                 postFixExpression.append[postFixOperators[-1]]
#                 del postFixOperators[-1]           

# print(postFixExpression)    


### Task No. 132 Evaluate Postfix
#----------------------------------------------------
### Task No. 133 Does a List Contain a Sublist?
# largeList = [1,2,3,4]
# smallList = [1,3]

# for i in range(len(largeList)):
#     if largeList[i:len(smallList)]==smallList:
#         print(">>>> IS SUBLIST <<<<")
#         quit()

# print(">>>> IS NOT A SUBLIST <<<<")  
      
# ### Task No. 134 Generate All Sublists of a List
# list = []
# while True:
#     inp = (input("Input a list item >>> "))
#     if inp == "":
#         break
#     list.append(inp)

# sublists = []
# for i in range(1,len(list)+1):
#     sub = []
#     for j in range(0,len(list)+1-i):
#         sub.append(list[j:j+i])
        
#     sublists.append(sub)   
    
# print(sublists) 
### Task No. 135 The Sieve of Eratosthenes
# lim = int(input("Enter the limit >>> "))
# nums = []
# for i in range(lim):
#     nums.append(i)

# nums[1] = 0
# p=2
# while p<lim:
#     for i in range(p*2,lim,p):
#         nums[i] = 0
    
#     p = p+1
#     while p<lim and nums[p]==0:
#         p=p+1
        
# for i in nums:
#     if i!=0:
#         print(i,end = "  ")