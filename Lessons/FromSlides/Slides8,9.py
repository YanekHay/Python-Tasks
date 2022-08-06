
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




