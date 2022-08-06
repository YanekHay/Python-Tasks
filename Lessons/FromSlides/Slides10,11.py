##### From slide No. 10
# Task No. 10.1

# import random
# num = random.randint(0,20)
# # Method 1
# #    V
# #    V
# # while num<=10:
# #     num = random.randint(0,20)    
# # print("\nEnd", num)

# # Method 2
# #    V
# #    V
# while True:
#     if num>10:
#         break
#     else:
#         num = random.randint(0,20)
        
# Task No. 10.2
# import random
# variants = "Rock","Paper","Scissors"
# userScore=0
# pcScore = 0
# maxPoints = 3
# while (userScore<maxPoints and pcScore<maxPoints):
#     pc = variants[random.randint(0,2)]
#     user = input("Rock, Paper, Scissors ...\n>>>>")
#     if(user in variants):
#         if (user=="Rock" and pc=="Scissors" or\
#             user=="Paper" and pc=="Rock" or\
#             user=="Scissors" and pc=="Paper"):
#             userScore+=1
#             print("You Won\nPC's score--->",pcScore,"\nYour score--->",userScore)
            
#         elif(pc=="Rock" and user=="Scissors" or\
#             pc=="Paper" and user=="Rock" or\
#             pc=="Scissors" and user=="Paper"):
#             pcScore+=1   
#             print("PC Won\nPC's score--->",pcScore,"\nYour score--->",userScore)
             
#         else:
#             print("Draw")       
#     else:
#         print("Wrong input\nInput again ----> Rock, Paper, Scissors\n>>>>")
    
# print("********************","You" if userScore==maxPoints else "PC","Won the GAME********************")

##### From slide No. 11  the smallest divisible
# Task No. 11.1
# a = 12
# b = 15
# num = max(a,b)

# while num%b != 0 or num%a != 0:
#     num+=1

# print(num)

# Task No. 11.2 ////Odd Even count
# oddCount = 0
# evenCount = 0
# for i in range(1,100):
#     if i%2==0:
#         evenCount+=1
#     else:
#         oddCount+=1

# print(f"Count of even numbers:{evenCount}\nCount of odd numbers:{oddCount}")

# Task No. 11.3 /////Fibonacci
# sequenceEnd = 40
# prev1 = 0
# prev2 = 1
# for i in range(0,sequenceEnd):
#     print(f"{prev1}")
#     next = prev1+prev2
#     prev1 = prev2
#     prev2 = next 
    


# Task No. 11.4 /////Letters and numbers
# text = input("Input some text with numbers\n>>>>>")
# digitCount = 0
# letterCount = 0
# for i in text:
#     if i.isdigit():
#         digitCount+=1
#     elif not i.isdigit() and i!=" ":
#         letterCount+=1
# print(f"The number of digits:{digitCount}\nThe number of letters:{letterCount}")

# Task No. 11.5 /////Sum of digits
# number = int(input("Enter some number\n>>>>>"))
# sum = 0
# #-----------Method 1
# # for i in str(number):
# #     sum+=int(i)

# #-----------Method 2
# while int(number)>0:
#     print(int(number%10))
#     sum+=int(number%10)
#     number/=10

# print(sum)

# Task No. 11.6 /////Factorial
# number = int(input("Enter a number\n>>>>"))

# if number==0:
#     print(1)
# else:   
#     fact = 1 
#     for i in range(1,number+1):
#         fact*=i

# print(fact)


# Task No. 11.7 /////UserData
# userAge = int(input("Enter Your age\n>>>>"))
# userSex = input("Enter Your Sex\n>>>>")
# if (18<=userAge<=20) and (userSex.lower()=="male"):
#     print("You Pass")
# else:
#     print("You don't pass")

######### My Tasks ########
#1. Գրեք ծրագիր, որ կտպի 1-ից մինչև տրված n թիվը միջակայքում գտնվող տարրերի զույգ թվանշանների գումարը
#2. Գրեք ծրագիր, որ կտպի տրված 4 միևնույն երկարությամբ թվերի համապատասխան դիրքերում գտնվող թվերի միջին թվաբանականը և դրանք հերթով կտպի
# oրինակ՝ տրված են 12, 13, 24, 65 թվերը։ Ծրագիրը պետք է տպի 1) 10,
#                                                           2) 14   


