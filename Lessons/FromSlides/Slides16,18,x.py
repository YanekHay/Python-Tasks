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
        
