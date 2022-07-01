############ Slide x.7 Invert Dict
# dict = {'a':'1','b':'2','c':'2'}
# inverted ={}
# for i in dict:
#     if dict[i] in inverted.keys():
#         inverted[dict[i]].append(i)
#     else:
#         inverted[dict[i]] = [i]

# print(inverted)

############ Slide x.5 Find the index
# numbers = [12,-50,123,-6,7,55,-33]
# inp = int(input("Enter a number >>> "))


# if inp in numbers:
#     print(numbers.index(inp))
    
# else:    
#     closestIndex =  0
#     for i in range(1,len(numbers)):
#         if abs(numbers[closestIndex]-inp)>abs(numbers[i]-inp):
#             closestIndex = i
#     print(numbers[closestIndex],"-------",closestIndex)

############ Slide x.6 Find the index
# order = [-1,150,-1,162,195,-1,1000,10,-1,180,130]
# people = []
# treeIndexes = []

# for i in range(len(order)):
#     if order[i]==-1:
#         treeIndexes.append(i)
#     else:
#         people.append(order[i])
        
# people.sort()

# step = len(treeIndexes)
# for i in treeIndexes:
#     people.insert(i,-1)
    
# print(people)
############ Slide 16.1
# dict = {
#     1:3,
#     2:-50,
#     3:23,
#     4:16,
#     5:98,
#     6:-2
# }

# sorted = sorted(dict,key = dict.get)
# for i in sorted:
#     print(i,":",dict[i])

############ Slide 16.2
# dict = {
#     1:3,
#     2:-50,
#     3:23,
#     4:16,
#     5:98,
#     6:-2
# }
# key = input("Enter a key >>> ")
# value = input("Enter a value >>> ")
# dict[key] = value
# print(dict)


############ Slide 16.3
# dict = {
#     '1':3,
#     '2':-50,
#     '3':23,
#     '4':16,
#     '5':98,
#     '6':-2
# }
# key = input("Enter a key >>> ")
# if key in dict.keys():
#     print("The key exists in the dictionary")
# else:
#     print("The key does not exist in the dictionary")

############ Slide 16.4
# dict1 = {'a': 50, 'b': 700}
# dict2 = {'a':23,'c': 400, 'd': 600}

# merged = dict1
# for i in dict2:
#     if i in merged:
#         merged[i]+=dict2[i]
#     else:
#         merged[i]=dict2[i]
# print(merged)
############ Slide 16.5
# mydict = {'a':1,'b':2,'c':12}
# p = 1
# for i in mydict:
#     p*=mydict[i]

# print(p)

############ Slide 16.6
# mydict = {
#     1:5,
#     2:8,
#     3:4,
#     4:1
# }
# sortedDict = sorted(mydict,key=mydict.get,reverse=True)[:3]
# res = {}
# for i in sortedDict:
#     res.setdefault(i,mydict[i])    
# print(res)

############ | Slide 18.1 Create 10 student dict, 
############ | Slide 18.2 Compute their average scores
############ | Slide 18.3 Tell wether a student is good or bad
############ | Slide 18.4 Tell which student has grades above 5
############ | Slide 18.5 Tell which student has grades above 5
############ | Slide 18.6 Name
#            V            #
# import random
# students = {}
# for i in range(1,11):
#     students[f"Student{i}"] = random.randint(1,10)

# avg = 0
# top5 = []
# bott5 = []
# for i in students:
#     avg+=students[i]
#     if students[i]<=6:
#         print(f"The {i} is a BAD  student with grade {students[i]}.")
#     else:
#         print(f"The {i} is a GOOD student with grade {students[i]}.")
#     if students[i]>5:
#         top5.append(i)
#     else:
#         bott5.append(i)

# for i in top5:
#     print(i,end =", ")    
    
# print("have ratings of more than 5")
# avg/=len(students.keys())
# print("\nThe average score of the students is",avg)

# name = input("Enter the name of the student >>> ")
# print("There is no student with such name." if f"'{name}'" in students.keys() else f"{name} has rating {students[name]}")
############ Slide 18.7 
# s  = 'a,2,b,5,c,8,a,4,e,11'
# s= s.split(",")
# list1 = [s[i] for i in range(0,len(s),2)]
# list2 = [s[i] for i in range(1,len(s),2)]
# newDict = {}

# for i,j in zip(list1,list2):
#     if i in newDict:
#         newDict[i]+=int(j)
#     else:
#         newDict[i] = int(j)
# print(newDict)


############ Slide 18.8
# text = "exercisec"
# newdict = {}
# for i in text:
#     newdict[i] = text.count(i)
 
# print(newdict)

############ Slide 18.9
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []

# for i in old_list[:]:
#     if(old_list.count(i)>1):
#         old_list.remove(i)

# print(old_list)

############ Slide 18.10
# questions =[
#     {
#         'Question':"Which company is known for publishing the Mario video game?",
#         'a': "Xbox",
#         'b': "Nintendo",
#         'c': "SEGA",
#         'd': "Electronic Arts",
#         'Answer':'b'
#     },
#     {
#         'Question':"In 1768, Captain James Cook set out to explore which ocean?",
#         'a': "Pacific Ocean",
#         'b': "Atlantic Ocean",
#         'c': "Indian Ocean",
#         'd': "Arctic Ocean",
#         'Answer':'a'
#     },
#     {
#         'Question':"What is actually electricity?",
#         'a': "A flow of water",
#         'b': "A flow of air",
#         'c': "A flow of electrons",
#         'd': "A flow of atoms",
#         'Answer':'c'
#     },
#     {
#         'Question':"Which of the following is not an international organisation?",
#         'a': "FIFA",
#         'b': "NATO",
#         'c': "ASEAN",
#         'd': "FBI",
#         'Answer':'d'
#     },
#     {
#         'Question':"Which of the following disorders is the fear of being alone?",
#         'a': "Agoraphobia",
#         'b': "Aerophobia",
#         'c': "Acrophobia",
#         'd': "Arachnophobia",
#         'Answer':'a'
#     },
#     {
#         'Question':"What is the speed of sound?",
#         'a': "120 km/h",
#         'b': "1,200 km/h",
#         'c': "400 km/h",
#         'd': "700 km/h",
#         'Answer':'b'
#     },
#     {
#         'Question':"Which is the easiest way to tell the age of many trees?",
#         'a': "To measure the width of the tree",
#         'b': "To count the rings on the trunk",
#         'c': "To count the number of leaves",
#         'd': "To measure the height of the tree",
#         'Answer':'b'
#     },
#     {
#         'Question':"Which did Viking people use as money?",
#         'a': "Rune stones",
#         'b': "Jewellery",
#         'c': "Seal skins",
#         'd': "Wool",
#         'Answer':'b'
#     },
#     {
#         'Question':"What was the first country to use tanks in combat during World War I?",
#         'a': "France",
#         'b': "Japan",
#         'c': "Britain",
#         'd': "Germany",
#         'Answer':'c'
#     },
#     {
#         'Question':"Which of the following animals can run the fastest?",
#         'a': "Cheetah",
#         'b': "Leopard",
#         'c': "Tiger",
#         'd': "Lion",
#         'Answer':'a'
#     }
# ]

# score = 0
# inp = input("Write Play to start the game (Exit to leave) >>> ")
# if(inp.lower()=="play"):
#     playing = True
#     import time
#     while True:
#         print("Question №",score+1,".")
#         print(questions[score]["Question"])
#         time.sleep(1)
#         print("A.",questions[score]['a'])
#         print("B.",questions[score]['b'])
#         print("C.",questions[score]['c'])
#         print("D.",questions[score]['d'])
        
#         ans = input("\nEnter the answer (a,b,c,d) >>> ")
#         if ans.lower() == "exit":
#             break
#         elif ans.lower()==questions[score]['Answer']:      
#             print("\nCorrect.\n\n")      
#             score+=1
#         else:
#             print(f"\nWrong answer...\nYour scored {score} points\nYOU LOST!!!")
#             break
#         if(score==10):
#             print("****-------- CONGRATULATIONS --------****\n            **** YOU WON ****")
#             break
        
    
##### Exercise 136: Reverse Lookup
# mydict = {
#     "a":5,
#     "b":6,
#     "c":18,
#     "f":5
# }

# srch = int(input("Enter the value to search >>> "))
# res = []
# for i in mydict:
#     if srch==mydict[i]:
#         res.append(i)

# print(res)


##### Exercise 137: Two Dice Simulation
# import random
# d = {}
# for i in range(1000):
#     d1 = int(random.randint(1,6))
#     d2 = int(random.randint(1,6))
#     sum = d1+d2
#     if sum in d:
#         d[sum] += 1
#     else: d[sum] = 1
# d2 = sorted(d)
# res = {}
# for i in d2:
#     res[i] = d[i]/1000*100
# print(res)

##### Exercise 138: Text Messaging
# buttons = {
# '1':".,?!:",
# '2':"ABC",
# '3':"DEF",
# '4':"GHI",
# '5':"JKL",
# '6':"MNO",
# '7':"PQRS",
# '8':"TUV",
# '9':"WXYZ",
# '0':" "
# }

# text = input("Enter some text >>>")
# res = ""
# for letter in text.upper():
#     for button in buttons:
#         if letter in buttons[button]:
#             for i in range(buttons[button].index(letter)+1):
#                 res += button

# print(res)

##### Exercise 139: Morse Code
# alphabet ={
#     'A' : '.-',
#     'B' : '-...',
#     'C' : '-.-.',
#     'D' : '-..',
#     'E' : '.',
#     'F' : '..-.',
#     'G' : '--.',
#     'H' : '....',
#     'I' : '..',
#     'J' : '.---',
#     'K' : '-.-',
#     'L' : '.-..',
#     'M' : '--',
#     'N' : '-.',
#     'O' : '---',
#     'P' : '.--.',
#     'Q' : '--.-',
#     'R' : '.-.',
#     'S' : '...',
#     'T' : '-',
#     'U' : '..-',
#     'V' : '...-',
#     'W' : '.--',
#     'X' : '-..-',
#     'Y' : '-.--',
#     'Z' : '--..',
#     '0' : '-----',
#     '1' : '.----',
#     '2' : '..---',
#     '3' : '...--',
#     '4' : '....-',
#     '5' : '.....',
#     '6' : '-....',
#     '7' : '--…',
#     '8' : '---..',
#     '9' : '----.',
# }

# text = input("Enter some text >>> ")
# res = ""
# for i in text.upper():
#     if(i not in alphabet):
#         continue
#     res = res + alphabet[i] + "  "

# print(res)

##### Exercise 140: Postal Codes
# codes = {
# 'Newfoundland' : 'A',
# 'Nova Scotia' : 'B',
# 'Prince Edward Island' : 'C',
# 'New Brunswick' : 'E',
# 'Quebec' : 'GHJ',
# 'Ontario' : 'KLMNP',
# 'Manitoba' : 'R',
# 'Saskatchewan' : 'S',
# 'Alberta' : 'T',
# 'British Columbia' : 'V',
# 'Nunavut' : 'X',
# 'Northwest Territories' : 'X',
# 'Yukon' : 'Y'
# }
# print(codes.values())
# while True:
#     inp = input("Enter your Postal Code >>> ")
#     if(len(inp.replace(" ",""))==6 and inp[0].upper() in i for j in codes.values() for i in j and inp[1].isdigit()):
#         break
#     else:
#         print("Wrong input, input again ")

# location = ""
# for i in codes:
#     if inp[0].upper() in codes[i]:
#         location = i

# print(f"The postal code is for {'rural'if inp[1]==0 else 'urban'} address in {location}")

##### Exercise 141: Write out Numbers in English
# words = {
#     '0' : "",
#     '1' : 'One',
#     '2' : 'Two',
#     '3' : 'Three',
#     '4' : 'Four',
#     '5' : 'Five',
#     '6' : 'Six',
#     '7' : 'Seven',
#     '8' : 'Eight',
#     '9' : 'Nine',
#     '10' : 'Ten',
#     '11' : 'Eleven',
#     '12' : 'Twelve',
#     '13' : 'Thirteen',
#     '14' : 'Fourteen',
#     '15' : 'Fifteen',
#     '16' : 'Sixteen',
#     '17' : 'Seventeen',
#     '18' : 'Eighteen',
#     '19' : 'Nineteen',
#     '20' : 'Twenty',
#     '30' : 'Thirty',
#     '40' : 'Forty',
#     '50' : 'Fifty',
#     '60' : 'Sixty',
#     '70' : 'Seventy',
#     '80' : 'Eighty',
#     '90' : 'Ninety',
#     '100' : 'Hundred'
# }

# while True:
#     num  = int(input("Enter a number between 0 and 999 >>>"))
#     if 0<=num<=999:
#         break
#     else:
#         print("Wrong input.\n")

# hundred = {
#     '1':int(num/100),
#     "00": '0' if num<100 else '100',
#     'and': "and" if num>100 and num%100>0 else ""
# }

# tenth = int(num/10)%10*10 if num-hundred['1']*100>=20 or num-hundred['1']*100<10 else num-hundred['1']*100
# unit = num%10 if num-hundred['1']*100>=20 or num-hundred['1']*100<10 else 0

# print(hundred,tenth,unit)

# print (f"{words[str(hundred['1'])]} {words[hundred['00']]} {hundred['and']} {words[str(tenth)]} {words[str(unit)]}".strip())

##### Exercise 142: Unique Characters
# text = input("Enter a text >>> ")
# chars = []
# for i in text:
#     if i not in chars:
#         chars.append(i)

# print(len(chars))     

##### | Exercise 143: Anagrams  
##### | Exercise 144: Anagrams Again 
##### V
# marks = "!@#$%^&*()_+/-=[]{}<>?`|',.:;~ "

# text1= input("Enter the first word >>> ")
# text2 = input("Enter the second word >>> ")

# for i in text1:
#     if i in marks:
#         text1 = text1.replace(i,"")
# for i in text2:
#     if i in marks:
#         text2 = text2.replace(i,"")

# text1 = text1.lower()
# text2 = text2.lower() 
 
# if text1!=text2 and len(text1) == len(text2):
#     for i in text1:
#          if i not in text2 or text2.count(i)!=text1.count(i):
#              print("The texts are NOT anagrams")
#              quit()
#     print("The texts ARE anagrams")
# else:
#     print("The texts are NOT anagrams")             

##### Exercise 145: Scrabble™ Score
# scoreTable = {
#     '1' : 'AEILNORSTU',
#     '2' : 'DG',
#     '3' : 'BCMP',
#     '4' : 'FHVWY',
#     '5' : 'K',
#     '8' : 'JX',
#     '10' : 'QZ'
# }

# text = input("Enter some text >>> ")
# points = 0
# for i in text.upper():
#     for key in scoreTable:
#         if i in scoreTable[key]:
#             points+=int(key)
#             break
# print(f"The word {text} has {points} points!")        

##### | Exercise 146: Create a Bingo Card
##### | Exercise 147: Checking for a Winning Card
##### | Exercise 148: Play Bingo
##### V
import random
from statistics import median_high
pulledCounts = []

def createCard():
    card = {
        'B':[],
        'I':[],
        'N':[],
        'G':[],
        'O':[]
    }
    ranger = 1
    for i in card:
        for j in range(5):
            card[i].append(random.randint(ranger,ranger+14))
        ranger+=15
    return card;   
 
def printCard(bing):
    for i in bing:
        print(f"{i} : ",end = "")
        for j in bing[i]:
            print(f"{j:<3}",end = "")
        print()
    print("\n\n")

def checkWin(card):
    global pulledCounts
    numbers = [i for i in range(1,76)]
    random.shuffle(numbers)
    calls = 0
############ pulling numbers until any row, column or diagonal fully consists of zeros
    for callNum in numbers:
        calls+=1
        finish = False
        for key in card:
            for i in range(5):
                if card[key][i]==callNum:
                    card[key][i]=0        
                      
        #Checking every Column                
        for i in range(5):
            col = True
            for key in card:
                if card[key][i]!=0:
                    col = False
                    break
            if col:
                finish = True
                break
        if finish:
            break
        #Checking every Row and Diagonals
        mainDiag = True
        secDiag = True
        for key in card:
            row = True #True means that the values are all zeros    
            main = 0 #for main diagonal
            sec = 4 #for secondary diagonal 
            if card[key][main]!=0:
                mainDiag = False
            main+=1
            if card[key][sec]!=0:
                secDiag = False
            sec-=1
            for i in card[key]:
                if i!=0: 
                    row = False
                    break
            if row:
                finish = True
                break
        
        if mainDiag or secDiag or finish:
            finish = True        
            break
    pulledCounts.append(calls)
    print(f"\n\n************** {calls} numbers were pulled completed **************")    
    printCard(card)    
# printCard(card)

for i in range(0,5):    
    card = createCard()
    printCard(card)
    checkWin(card)

# print(f"Minimum number of calls: {min(pulledCounts)}\nMedian number of calls: {median_high(pulledCounts)}\nMaximum number of calls: {max(pulledCounts)}")
    # for key in card:
    #     for j in range(5):
    #         if 
#####

