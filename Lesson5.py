#Exercises From book
#Ex. 35  //8.4
# n = int(input("Input a number >>>"))
# print("Even" if n%2==0 else "Odd")

#Ex. 36  //8.1
# humanAge = float(input("Input age >>>"))
# if(humanAge>=0):
#     if(humanAge>21):
#         print(humanAge , " years in dog's years is" , (humanAge-21)/4+2, "years")
#     else:
#         print(humanAge , " years in dog's years is" , (humanAge/10.5), "years")
# else:
#     print("Incorrect input:\nYour input has to be a positive number")

#Ex. 37 //8.2
# letter = input("Input a letter >>>").lower()
# if len(letter)== 1 and not (letter.isdigit()) :
#     if (letter == "a" or letter == "o" or letter == "u" \
#         or letter == "i" or  letter == "e"):
#         print("Letter is Vowel")
#     else:    
#         print("Letter is Consonant")
# else: print("Wrong input!!!")

#Ex. 38  //
# sideCount = int(input("Input the number of sides of shape\n[3,10]>>>"))
# if sideCount==3:
#     message = "triangle"
# elif sideCount==4:
#     message = "quadrilateral"
# elif sideCount==5:
#     message = "pentagon"
# elif sideCount==6:
#     message = "hexagon"
# elif sideCount==7:
#     message = "heptagon"
# elif sideCount==8:
#     message = "octagon"
# elif sideCount==9:
#     message = "nonagon"
# elif sideCount==10:
#     message = "decagon"
# else:
#     message ="Input has to be in [3,10]"

# print("A shape with", sideCount,"sides is called",message)

#Ex. 39
# month = input("Input the month >>>")
# if month=="January" or month == "March" or month == "May" or\
#    month=="July" or month=="August" or month=="October" or month=="December":
#     print(month,"has 31 days in it")
# elif month=="February":
#     dayCount = 28
#     print(month,"has either 28 or 29 days in it")
# else:
#     print(month,"has 30 days in it")

#Ex. 40
# hammer = 130
# gas = 106
# alarm = 70
# room = 40

# inp = int(input("Input the level of sound >>> "))
# if(inp==hammer):
#     print("Отбойный молоток")
# elif(inp ==gas):
#     print("Газовая газонокосилка")
# elif(inp==alarm):
#     print("Будильник")
# elif(inp==room):
#     print("Тихая комната")
# elif(inp<hammer and inp>gas):
#     print("Between {Отбойный молоток} and {Газовая газонокосилка}")
# elif(inp<gas and inp>alarm):
#     print("Between {Газовая газонокосилка} and {Будильник}")
# elif(inp<gas and inp>alarm):
#     print("Between {Будильник} and {Тихая комната}")
# else:
#     print("There is no compatable source")

#Ex. 41
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# if(a==b and a==c):
#     print("The triangle is isosceles")
# elif(a==b or b==c or a==c):
#     print("The triangle is equilateral")
# else:
#     print("The triangle has unequal sides")
    
    
#Ex. 42
# C =  261.63/16
# D =  293.66/16
# E =  329.63/16
# F =  349.23/16
# G =  392.00/16
# A =  440.00/16
# B = 93.88/16

# userInput = input("Input the note >>>")

# if(userInput[0] == "C"):
#     print("Frequency of",userInput,"is",2**int(userInput[1])*C)
# elif(userInput[0] == "D"):
#     print("Frequency of",userInput,"is",2**int(userInput[1])*D)
# elif(userInput[0] == "E"):
#     print("Frequency of",userInput,"is",2**int(userInput[1])*E)
# elif(userInput[0] == "F"):
#     print("Frequency of",userInput,"is",2**int(userInput[1])*F)
# elif(userInput[0] == "G"):
#     print("Frequency of",userInput,"is",2**int(userInput[1])*G)
# elif(userInput[0] == "A"):
#     print("Frequency of",userInput,"is",2**int(userInput[1])*A)
# elif(userInput[0] == "B"):
#     print("Frequency of",userInput,"is",2**int(userInput[1])*B)
# else:   
#     print("Something is wrong")

#Ex. 43
# C =  261.63
# D =  293.66
# E =  329.63
# F =  349.23
# G =  392.00
# A =  440.00
# B = 93.88

# userInput = float(input("Input the note frequency >>> "))
# if(abs(userInput-C)<1):
#     print("C4")
# elif(abs(userInput-D)<=1):
#     print("D4")
# elif(abs(userInput-E)<=1):
#     print("E4")
# elif(abs(userInput-F)<=1):
#     print("F4")
# elif(abs(userInput-G)<=1):
#     print("G4")
# elif(abs(userInput-A)<=1):
#     print("A4")
# elif(abs(userInput-B)<1):
#     print("B4")
# else:
#     print("There is no note that matches to the given frequency")

#Ex. 44
# userInput = int(input("Input the note frequency >>> "))

# if(userInput==1):
#     print("Джордж Вашингтон ")
# elif(userInput==2):
#     print("Томас Джефферсон")
# elif(userInput==5):
#     print("Авраам Линкольн ")
# elif(userInput==10):
#     print("Томас Джефферсон")
# elif(userInput==20):
#     print("Эндрю Джексон ")
# elif(userInput==50):
#     print("Улисс Грант")
# elif(userInput==100):
#     print("Бенджамин Франклин")
# else:
#     print("There is no such a banknote")

#Ex. 45
# userInput = input("Input the note frequency >>> ")
# if(userInput=="January 1"):
#     print("New Year")
# elif(userInput=="June 1"):
#     print("the Day of Canada")
# elif(userInput=="December 25"):
#     print("Mery Christmas")
# else:
#     print("There are no holidays on the given date")

#Ex 46
# userInput = input("Input the cell coordinates >>> ")
# #print("Black" if (ord(userInput[0].lower())-97+int(userInput[1]))%2==1 else "White")
# ###### Second Variant ######
# odd = "a,c,e,g"
# even = "b,d,f,h"
# if userInput[0] in odd and int(userInput[1])%2 ==0 or userInput[0] in even and int(userInput[1])%2==1:
#     print("White")
# elif userInput[0] in odd and int(userInput[1])%2 ==1 or userInput[0] in even and int(userInput[1])%2==0:
#     print("Black")
#Ex 47
# inputMonth =   input("Month >>> ")
# inputDay = int(input("Day   >>> "))

# daysMarch = 59
# daysJune = 151
# daysSeptember = 243
# daysDecember = 334

# if(inputMonth == "January"):
#     month = 1
#     days = 1
# elif(inputMonth =="February"):
#     month = 2
#     days = 31
# elif(inputMonth =="March"):
#     month = 3
#     days = 59
# elif(inputMonth =="April"):
#     month = 4
#     days = 90
# elif(inputMonth =="May"):
#     month = 5
#     days = 120
    
# elif(inputMonth =="June"):
#     month = 6
#     days = 151
    
# elif(inputMonth =="July"):
#     month = 7
#     days = 181
# elif(inputMonth =="August"):
#     month = 8
#     days = 212
# elif(inputMonth =="September"):
#     month = 9
    
#     days = 243
# elif(inputMonth =="October"):
#     month = 10
#     days = 273
# elif(inputMonth =="November"):
#     month = 11
#     days = 304
# elif(inputMonth =="December"):
#     month = 12
#     days = 334
    
    
# if(inputDay+days>=daysMarch+22 and inputDay+days<daysJune+21 ):
#     print("Spring")
# elif(inputDay+days>=daysJune+21 and inputDay+days<daysSeptember+22):
#     print("Summer")
# elif(inputDay+days>=daysSeptember+22 and inputDay+days<daysDecember+21):
#     print("Autumn")
# else:
#     print("Winter")

#Ex. 48
## Has the same principle as Ex. 47 ⬆️⬆️⬆️

#Ex.49
# inpYear = int(input("Enter the year of your birth >>> "))
# if inpYear%12==8:    yname = "Dragon"
# elif inpYear%12==9:  yname ="Snake"  
# elif inpYear%12==10:  yname ="Horse"  
# elif inpYear%12==11:  yname ="Goat"
# elif inpYear%12==0:  yname ="Monkey"
# elif inpYear%12==1:  yname ="Rooster"
# elif inpYear%12==2:  yname ="Dog"
# elif inpYear%12==3:  yname ="Pig"
# elif inpYear%12==4:  yname ="Rat"
# elif inpYear%12==5:  yname ="Ox"
# elif inpYear%12==6: yname ="Tiger"
# elif inpYear%12==7: yname ="Rabbit"  

# print("The name of your birth year is",yname)

#Ex.50
# inp = float(input("Input the magnitute of earthquake >>> "))
# if inp<2.0:               msg = "Минимальное"
# elif inp>=2.0 and inp<3.0:  msg = "Очень слабое"
# elif inp>=3.0 and inp<4.0:  msg = "Слабое"
# elif inp>=4.0 and inp<5.0:  msg = "Промежуточное"
# elif inp>=5.0 and inp<6.0:  msg = "Умеренное"
# elif inp>=6.0 and inp<7.0:  msg = "Сильное"
# elif inp>=7.0 and inp<8.0:  msg = "Очень сильное"
# elif inp>=8.0 and inp<10.0: msg = "Огромное"
# elif inp>=10.0:           msg = "Разрушительное"

# print(msg)

#Ex. 51




#Ex 8.3
# year = int(input("Input the year >>> "))

# if(year%4==0):
#     print("Year is leap")
# else:
#     print("Year is not leap")

#Ex 8.5
# import random

# userPoints=0
# pcPoints=0

# pc = int(random.randint(0,5))
# user = int(input("Input a number between 0 and 5 >>> "))
# if(user == pc):
#     print("✔️\n")
#     userPoints+=1
# else:
#     print("❌\n")
#     pcPoints+=1

# pc = int(random.randint(0,5))
# user = int(input("Input a number between 0 and 5 >>> "))
# if(user == pc):
#     print("✔️\n")
#     userPoints+=1
# else:
#     print("❌\n")
#     pcPoints+=1

# if userPoints==2:
#     print("You Won")
# elif pcPoints==2:
#     print("You Lost")
# else:
#     pc = int(random.randint(0,5))
#     user = int(input("Input a number between 0 and 5 >>> "))
#     if(user == pc):
#         print("✔️\n")
#         userPoints+=1
#     else:
#         print("❌\n")
#         pcPoints+=1
        
#     if userPoints==2:
#         print("You Won")
#     elif pcPoints==2:
#         print("You Lost")


#Ex. 9.1
# a= int(input("a = "))
# b= int(input("b = "))

# if(a>b):
#     print(a)
# elif(a==b):
#     print("The given numbers are equal")
# else:
#     print(b)
    
#Ex. 9.2
# a= int(input("a = "))
# b= int(input("b = "))
# c= int(input("c = "))

# if(a>b):
#     if(a>c):
#         print("\nThe first person is the oldest\n")
#         if(b>c):
#             print("The thid person is the youngest\n")
#         elif(b==c):
#             print("The second and the third people are the youngest with the same age\n")   
#         else:
#             print("The second person is the youngest\n")        
#     elif(a==c):
#         print("\nThe first and third people are the oldest with the same age\n")
#         print("The second person is the youngest\n")
#     elif(c>a):
#         print("The third person is the oldest\n")        
#         if(a==b):
#             print("The first and the second people are the youngest with the same age")
#         else:
#             print("The second person is the youngest")

        
# elif(b>a):
#     if(b>c):
#         print("\nThe second person is the oldest\n")
#         if(a>c):
#             print("The third person is the youngest\n")
#         elif(a==c):
#             print("The first and the third people are the youngest with the same age\n")   
#         else:
#             print("The first person is the youngest\n") 
                   
#     elif(b==c):
#         print("\nThe second and third people are the oldest with the same age\n")
#     elif(c>b):
#         print("The third person is the oldest\n")
#         if(a==c):
#             print("The first and the second people are the youngest\n")
#         else:
#             print("The first person is the youngest\n")
# elif(c>a):
#     if(c>b):
#         print("The third person is the oldest")
#         if(a>b):
#             print("The second person is the youngest")

# #Ex. 9.3
# n= int(input("n = ")) 
# revN = n%10*1000 + int(n/10)%10*100 + int(n/100)%10*10 + int(n/1000)
# print(revN)

#Ex. 9.4
# age= int(input("Age >>> "))
# sex = input("Male or Female >>> ")
# marial = input("Yes or No >>>")

# if(sex=="Female"):
#      work = "Urban areas"
# else:
#     if(age>20 and age<40):
#         work = "Anywhere"
#     elif(age>40 and age<60):
#         work = "Urban areas"
#     else:
#         work = "ERROR"

# print(work)

#Ex 9.5
# import random
# import time

# start = input("Yes or No")

# if(start=="Yes"):
#     print(1)
#     time.sleep(0.5)
#     print(2)
#     time.sleep(0.5)
#     print(3)
#     time.sleep(0.5)
#     print("Ready!")
#     randNum = random.randint(0,2)
#     if randNum == 0:
#         pc = "Rock"
#     elif randNum ==1:
#         pc = "Paper"
#     else:
#         pc = "Scissors"

#     user = input("Rock, Paper, Scissors ...\n>>> ")
#     if(user == "Rock"):
#         if(pc=="Rock"):
#             print("Draw")
#         elif(pc=="Paper"):
#             print("You Won")
#         else:
#             print("You Lost")
            
#     elif(user=="Paper"):
#         if(pc=="Rock"):
#             print("You Won")
#         elif(pc=="Paper"):        
#             print("Draw")
#         else:
#             print("You Lost")
            
#     elif(user=="Scissors"):
#         if(pc=="Rock"):
#             print("You Lost")        
#         elif(pc=="Paper"):
#             print("You Won")
#         else:
#             print("Draw")
#     else:
#         print("ERROR")
# else: print("End Game")
    

#Ex. 9.6
# import random
# pc = random.randint(1,10000000)
# print(pc)
# inp = int(input("Input the number of followers >>> "))
# if pc*1.2<inp:
#     print("Is Blogger")
# else:
#     print("Is not a Blogger")

#Ex. 9.7
# userTime = 12/3*1.1
# print(12/userTime, "km per minute")




#####################   MY TASKS  ######################
# 1.Write a program which will say if the given 2 digit number is symetric or not 
# (A number is symetric when it is the same when read from left to right or opposite)

# 2.Write a program which will say if it is
                                            # Morning(noon)     05:00 to 12:00 .
                                            # Afternoon         12:00 to 17:00 .
                                            # Evening           17:00 to 21:00 .
                                            # Night             21:00 to 04:00 .




