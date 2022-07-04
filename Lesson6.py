# Task No. 62 From book

# reds = ("1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36")
# greens = ("0","00")

# import random

# randNum = random.randint(0,37)
# if randNum==37: randNum = "00"

# if(str(randNum) in reds):
#     color = "Red"
# elif(str(randNum) in greens):
#     print("Выпавший номер: ",randNum,"...\nВыигравшая ставка: ",randNum)
#     quit()
# else: color = "Black"

# if(randNum not in greens):    
#     if(randNum%2==1): EvenOdd = "Odd"
#     else: EvenOdd = "Even"        
        
#     if(1<=randNum<=18): numRange = "From 1 to 18"
#     elif(19<=randNum<=36): numRange = "From 19 to 36"    

#     print("Выпавший номер:   ",randNum,"\nВыигравшая ставка:",randNum,"\nВыигравшая ставка:",color,"\nВыигравшая ставка:",EvenOdd,"\nВыигравшая ставка:",numRange)            

#

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


####### TASKS FROM THE BOOK #######
#Task No. 63 Average
# inp =  float(input("Input number >>>>"))
# if(inp==0):
#     print("ERROR. ---> No numbers entered.")
# else:    
#     sum = inp
#     q = 1
#     while True:
#         inp = float(input("Input number >>>>"))
#         if(inp==0):
#             break
#         sum+=inp
#         q+=1
        
#     print(sum/q)

#Task No. 64 Discount Table $4.95, $9.95, $14.95, $19.95 and $24.95
# purchases = 4.95, 9.95, 14.95, 19.95, 24.95
# for i in purchases:
#     print("{0:.2f}".format(i*0.4))

#Task No. 65 Temperature Conversion Table
# print("Table of Conversion\n[Celsius]      [Fahrenheit]")
# for Cels in range(10,101,10):
#     print(f" {Cels}  °C  -----  {Cels * 1.8 + 32}  °F")

#Task No. 66 No More Pennies
# firstLine=0
# secondLine = 0
# while True:
#     inp = input("Input number >>>>")
#     if(inp==""):
#         break
#     else:
#         firstLine+=float(inp)
        
# secondLine = int(firstLine) if firstLine%5<2.5 else int(firstLine+1)
# print(f"{firstLine}\n{secondLine}")            

#Task No. 67 Compute the Perimeter of a Polygon
# import math
# a = "5"

# x1 = float(input("Enter the first x-coordinate >>> "))
# y1 = float(input("Enter the first y-coordinate >>> "))
# x0 = x1
# y0 = y1
# Perimeter = 0
# while True:
#     x2Inp = input("Enter the first x-coordinate (blank to quit) >>> ")
#     if(x2Inp==""):        
#         break
#     y2Inp = input("Enter the first y-coordinate (blank to quit) >>> ")    
#     x2 = float(x2Inp)
#     y2 = float(y2Inp)
#     Perimeter += math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
#     print(x1,":",x2,"\n",y1,":",y2,"\n")
#     x1=x2
#     y1=y2
#     print(x1,":",x2,"\n",y1,":",y2,"\n")
# Perimeter += math.sqrt(math.pow(x0-x2,2)+math.pow(y0-y2,2))
# print(Perimeter)

#Task No. 68 Average Grade Point
# sum = 0
# q = 0
# while True:
#     inpGrade = input("Input your grade >>> ")
    
#     if(inpGrade==""):
#         break
#     if(inpGrade == "A+"):
#         gradePoint = 4.0
#     elif(inpGrade == "A"):
#         gradePoint = 4.0
#     elif(inpGrade == "A-"):
#         gradePoint = 3.7
#     elif(inpGrade == "B+"):
#         gradePoint = 3.3
#     elif(inpGrade == "B"):
#         gradePoint = 3.0
#     elif(inpGrade == "B-"):
#         gradePoint = 2.7    
#     elif(inpGrade == "C+"):
#         gradePoint = 2.3
#     elif(inpGrade == "C"):
#         gradePoint = 2.0
#     elif(inpGrade == "C-"):
#         gradePoint = 1.7
#     elif(inpGrade == "D+"):
#         gradePoint = 1.3
#     elif(inpGrade == "D"):
#         gradePoint = 1.0
#     elif(inpGrade == "F"):
#         gradePoint = 0
#     else:
#         print("ERROR")
#         quit()
#     sum+=gradePoint
#     q+=1

# print(sum/q)


#Task No. 69 Average Grade Point

# totalPrice = 0
# while True:
#     guest = input("Input the Age of the guset (Blank to quit) >>> ")
#     if(guest==""):        
#         break
#     elif(not guest.isdigit() or int(guest)<0):
#         print("WRONG INPUT")
#         quit()
#     guest = int(guest)
#     if(3<=guest<=12):
#         totalPrice+=14
#     elif(guest<=2):
#         totalPrice+=0
#     elif(guest>=65):
#         totalPrice+=18
#     else:
#         totalPrice+=23

# print("The total income from guests is {0:.2f} $".format(totalPrice))


#Task No. 70 Parity Bits
# while True:
#     userInp = input("Input an octet >>> ")
#     if(userInp == ""):
#         break
#     elif(len(userInp)!=8 or not userInp.isdigit()):
#         print("Wrong Input")
#         quit()
#     parityBit = "Even" if userInp.count("1")%2==0 else "Odd"
#     print(parityBit)

#Task No. 71 Pi
# end = 15
# pi = 3
# sign = 1
# for i in range(4,end,2):    
#     pi += sign*4/(i*(i-1)*(i-2))
#     sign *= -1
# print(pi)

#Task No. 72 Fizz-Buzz

# for i in range(1,100):
#     if(i%3==0 and i%5==0):
#         word = f"{i} or FizzBuzz"
#     elif(i%3==0):
#         word = f"{i} or Fizz"
#     elif(i%5==0):
#         word = f"{i} or Buzz"
#     else:
#         word = i
#     print(f"{i}) {word}")

#Task No. 73 Caesar Cipher
# text = input("Enter some text.\n>>>> ")
# key = 3
# text = text.upper()
# encoded = ""
# for i in text:
#     encoded = (f"{encoded}{chr((ord(i)+-64+26+key)%26+64)}")
    
# print(f"The encoded text is ---> {encoded}")

#Task No. 74 Square Root
# num = float(input("Input a number >>> "))
# guess = num/2
# while abs(guess*guess-num)>0.000001:
#     guess = (guess+(num/guess))*0.5
# print(guess)

#Task No. 75 Is a String a Palindrome?
# text = input("Input some text >>> ")
# revText = ""
# for i in text:
#      revText = f"{i}{revText}"
    
# print("The text is Palindrome" if(revText == text ) else "The text is not Palindrome")
# print(revText)

#Task No. 76 Is a String a Palindrome with ignoring the spaces?
# text = input("Input some text >>> ")
# newText = ""
# revText = ""
# for i in text:
#     if(i!=" "):
#         revText = f"{i}{revText}"
#         newText = f"{newText}{i}"
    
    
# print("The text is Palindrome" if(revText == newText ) else "The text is not Palindrome")
# print(revText)


#Task No. 77 Multiplication Table
# print(f"{' ': >2}",end="")
# for i in range(1,11):
#     print (f"{i: >5}",end="")
# print("\n")
# for i in range(1,11):
#     print(f"{i:>2}",end="")
#     for j in range(1,11):
#         print(f"{i*j: >5}",end="")
#     print("\n")


#Task No. 78 Collatz conjecture

# while True:
#     n = (input("Enter a number >>> "))
#     if(n==""):
#         break
#     n = int(n)
#     steps = 0
#     while n>1:
#         if(n%2==0):
#             n = n/2
#         else:
#             n = 3*n+1
#         steps+=1
#         print(n)
    
#     print(f"Total steps:{steps}\n-----------Next Number----------")


#Task No. 79 Greatest common divisor
# n = int(input("n = "))
# m = int(input("m = "))

# d = min(m,n)
# while n%d!=0 or m%d != 0:
#     d-=1
    
# print(d)

#Task No. 80 Prime Factors
# n = int(input("n = "))
# factor = 2
# print(f"Factors of {n} are ...")
# while(factor <= n):
#     if(n%factor==0):
#         n=n/factor
#         print(factor)
#     else:
#         factor+=1

#Task No. 81 Binary to Decimal
# n = int(input("n = "))
# binary = ""
# while n>=1:
#     binary = f"{n%2}{binary}"
#     n = int(n/2)
#     #print(n)

# print(binary)

#Task No. 82 Decimal to Binary
# binary = (input("Enter a binary number >>> "))
# n = 0
# l=len(binary)
# for i in binary:
#     #Computing the power of 2
#     digit = int(i)
#     for p in range(1,l):
#         digit*=2
#     l-=1    
#     n+=digit    


# print(n)

#Task No. 83 Maximum Integer

# import random

# q = 0
# num = random.randint(1,100) 
# max = num
# for i in range(1,100):
#     num = random.randint(1,100)
    
#     if num>max:
#         max = num
#         print(f"{i:<2}) {num:<6}<=== max is Updated here")
#         q+=1
#     else:
#         print(f"{i:<2}) {num:<6}")     
        
# print(f"The maximum number is {max}\n It was Updated {q} times")  
# import random        
# coin = "T", "H"
# totalFlipCount = 0
# succeded = 0
# for i in range(random.randint(3,10)):
#     #print("\n")
#     hCount = 0
#     tCount = 0
#     fl = 0
#     rng = random.randint(4,10)
#     coll = ""
#     while tCount<3:
#         coll = ""
#         for j in range(rng):
#             c = coin[random.randint(0,1)]            
#             if(c=="T"):
#                 tCount+=1
#             else:
#                 tCount=0
#             coll = f"{coll}{c},"
#         fl+=1
        
#     print(f"{coll} ({fl} Flips)") 
#     succeded+=1
#     totalFlipCount+=fl

# print(f"\nOn average {totalFlipCount/succeded:.2f} Flips were needed\n")    
