#Slide 15.3

# symbols = "!@#$%&*"
# password = ""
# while True:
#     password = input("Enter a password >>> ")
#     synbCount = 0
#     numCount = 0
#     if(password[0].isupper()):
#         for i in range(len(password)):
#             if password[i] in symbols:
#                 synbCount+=1
#             elif password[i].isdigit():
#                 numCount+=1
#         print(synbCount,numCount)
#         if synbCount<2 or numCount<2:
#             print("The password must contain at least 2 numbers, 2 symbols and must begin with capital letter\n")
#             continue
#         else:
#             break
#     else:
#         print("The password must contain at least 2 numbers, 2 symbols and must begin with capital letter\n")
#         continue
        
# print("Password is set to >>>",password)      


#Slide 15.9
## V 1.0
# import random
# names = ["Daniel","John","George","Abraham","Joseph"]
# people = names[:]
# chooseRandom=[]
# for person in people: 
#     while True:
#         rndIndex = random.randint(0,len(names)-1)
#         pull = names[rndIndex]
#         if(len(names)==1 and names[0]==pull):
#             names = people[:]
#             chooseRandom.clear
#             continue
#         if(pull == person):
#             continue
#         else:
#             chooseRandom.append(pull)
#             del names[rndIndex]
#             break
        

# print("People >>>",people)
# print("Pulls  >>>",chooseRandom) 

# V 2.0
# import random
# names = ["Daniel","John","George","Abraham","Joseph"]
# random.shuffle(names)
# for i in range(0,len(names)):
#     print(f"{names[i]}---{names[(i+1)%len(names)]}")

