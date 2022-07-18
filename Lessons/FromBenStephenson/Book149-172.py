fileLocation = "C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\FromBenStephenson\\Files\\"


### Exercise 150: Display the Tail of a File
# with open("C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\FromBenStephenson\\Files\\names.txt","rt") as file:
#     lines = file.readlines()

# n = int(input("Enter the number of lines to be displayed >>> "))
# for i in range(n):
#     print(lines[i][:-1])

### Exercise 151: Concatenate Multiple Files
# fileList = []
# while True:
#     inp = input("Enter the file name with extention >>> ")
#     if inp == "":
#         break
#     else:
#         fileList.append(inp)
# thisLocation = "C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\FromBenStephenson\\Files\\"
# def cat(files:list[str]):
#     l = []
#     for i in files:
#         with open(thisLocation+i,"rt") as file:
#             one = file.readlines()
#         l.extend(one)
#         l[-1] = l[-1] + "\n"
#     with open(thisLocation+"Concatinated.txt","w") as f:
#         for i in l:
#             f.write(i)
# cat(fileList)

### Exercise 152: Number the Lines in a File
# with open("C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\FromBenStephenson\\Files\\names.txt","rt") as names:
#     n = names.readlines()

# newlist = ""
# row = 1
# for i in n:
#     newlist+=(f"{str(row)}) {i}")
#     row+=1

# with open("C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\FromBenStephenson\\Files\\result152.txt","w") as res:
#     res.write(newlist)
    
### Exercise 153: Find the LongestWord in a File
# with open("C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\FromBenStephenson\\Files\\names.txt","rt") as names:
#     n = names.readlines()

# word = n[0]
# for i in n:
#     if(len(i)>len(word)):
#         word = i
        
# print(f"The longest word is {word}")

### Exercise 154: Letter Frequencies
# def getfileText(file):
#     with open(file,"rt") as names:
#         n = names.readlines()
#     filetext = ""
#     ignore = " !@#$%^&*()_+/*<>?~`':;,.\n"
#     for i in n:
#         for symbol in ignore:
#             i = i.replace(symbol,"")
#         filetext+=i.upper()
#     return filetext
    
# def findFrequencies(text:str)->dict:
#     res = {}
#     for letter in text:
#         if letter in res.keys():
#             res[letter]+=1
#         else:
#             res[letter]=1
#     ## Sorting the result
#     final = {}
#     for i in sorted(res,key=res.get,reverse=True):
#         final[i] = res[i]
        
#     return final

# fileText= getfileText("C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\FromBenStephenson\\Files\\names.txt")

# frequencies = findFrequencies(fileText)

# for item in frequencies.items():        
#     print(item)

### Exercise 155: Words that OccurMost


# def getCleanWords(filename:str)->list:
#     punctuation = "-!@#$%^&*()_+/*<>?~`':;,.\n"
#     with open(fileLocation+filename,"rt") as file:
#         f = file.readlines()
#     words = []
#         ### Getting all words
#     for line in f:
#         for mark in punctuation:
#             line = line.replace(mark,"")
#         line = line.split(" ")
#         nline = []
#         for i in line:
#             if i!='':
#                 nline.append(i)
#         words.extend(nline)
#     return words
        
        
# def findFrequencies(wordList:list)->dict:
#     freq = {}
#     for i in wordList:
#         if i in freq.keys():
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq

# def getFrequent(freq:dict):
#     res = {}
#     for i in freq:
#         if freq[i]>3:
#             res[i] = freq[i]
#     return res


# inp = input("Enter the file name with extention >>> ")
# print(getCleanWords(inp))
# print(getFrequent(findFrequencies(getCleanWords(inp))))

### Exercise 156:Sum a Collection of Numbers
# sum = 0
# while True:
#     inp = input("Enter a number >>> ")
#     if inp =="":
#         print(f"The sum of inputs is {sum}")
#         break
#     else:
#         try:
#             inp = float(inp)
#         except:
#             print("The total input must be a number!")
#         else:
#             sum += inp    
#             print(f"Current sum is {sum}")

### Exercise 157: Both Letter Grades and Grade Points
# letterGrades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
# numGrades =    [4   ,3.9,3.7 ,3.3 ,3  ,2.7 ,2.3 ,2  ,1.7 ,1.3 ,1  ,0.7 , 0]

# while True:
#     grade = input("Enter a grade >>> ")
#     if grade == "":
#         break
#     else:
#         try:
#             grade = float(grade)
#         except:
#             if grade in letterGrades:
#                 print(f"Your numeric grade is {numGrades[letterGrades.index(grade)]}")
#             else:
#                 print("Wrong grade is entered!")
#         else:
#             if numGrades[-1]<=grade and grade<=numGrades[0]:
#                 for i in range(1,len(numGrades)):
#                     if numGrades[i]<=grade and numGrades[i-1]>=grade:
#                         print(f"Your grade with letter is {letterGrades[i]}")
#                         break
#             else:
#                 print("Wrong grade is entered!")
                

### Exercise 158:Remove Comments
# while True:
#     inpfile = input("Enter the input file name  >>> ")
#     try:
#         with open(fileLocation + inpfile,"rt") as f:
#             lines = f.readlines()
#     except:
#         print("Wrong file name entered!!!")
#         inpfile = ""
#     else:
#         break


# newlines = []
# for line in lines:
#     if len(line.lstrip())!=0 and line.lstrip()[0] != "#":
#         newlines.append(line)

# outFile = input("Enter the output file name >>> ")
    
# with open(fileLocation+outFile,"w") as newfile:
#     newfile.writelines(newlines)

# Exercise 159:TwoWord Random Password
# import random

# def generatePassword(file = fileLocation+"PasswordWords.txt"):
#     with open(file,"rt") as f:
#         line = f.readline()
#     words = line.split(" ")
#     word1 = words[random.randint(0,len(words)-1)].lower().capitalize()
    
#     while len(word1)<3 or len(word1)>7:
#         word1 = words[random.randint(0,len(words)-1)].lower().capitalize()
        
#     word2 = words[random.randint(0,len(words)-1)].lower().capitalize()
#     while word2==word1 or len(word2)<3 or len(word1+word2)>10 or len(word1+word2)<7:
#         word2 = words[random.randint(0,len(words)-1)].lower().capitalize()

#     return word1+word2

# print(generatePassword())

#### Making a file one liner    
# with open(fileLocation+"PasswordWords.txt","rt") as f:
#     lines = f.readlines()
# oneline = ""
# for line in lines:
#     oneline += line[:-1] + " "

# with open(fileLocation+"PasswordWords.txt","w") as f:
#     f.write(oneline)


### Exercise 160:WeirdWords

# def findadjanctions(file):
#     with open(file,"rt") as f:
#         lines = f.readlines()
#     punctuation = "-!@#$%^&*()_+/*<>?~`':;,.\n"
#     rulebreakers = set()
#     rulefollowers = set()
#     for line in lines:
#         for mark in punctuation:
#             line = line.replace(mark," ")
#         linewords = line.split(" ")
#         for word in linewords:
#             if len(word)>=2:
#                 for pair in range(1,len(word)):
#                     ### IE
#                     if word[pair:pair+2].lower() == "ie":
#                         if word[pair-1].lower()=="c":
#                             rulebreakers.add(word)
#                         else:
#                             rulefollowers.add(word)
#                     ### EI        
#                     elif word[pair:pair+2].lower() == "ei":
#                         if word[pair-1].lower()=="c":
#                             rulefollowers.add(word)
#                         else:
#                             rulebreakers.add(word)
#                     ### IE      
#                     if word[pair-1:pair+1].lower() == "ie":
#                         if pair>=2 and word[pair-2]=="c":
#                             rulebreakers.add(word)
#                         else:
#                             rulefollowers.add(word)
#                     ### EI         
#                     elif word[pair-1:pair+1].lower() == "ei":
#                         if pair>=2 and word[pair-2]=="c":
#                             rulefollowers.add(word)
#                         else:
#                             rulebreakers.add(word)
                    
                    
            
#     return [list(rulebreakers),list(rulefollowers)]

# print(findadjanctions(fileLocation+"CoralReef.txt"))


### Exercise 161:What’s that Element Again?
####Creating a file with info about chemicals
# import mendeleev
# elements = mendeleev.get_all_elements()
# with open(fileLocation+"chemicals.txt","w") as f:
#     for element in elements:
#         f.write(str(element)+"\n")

# def getChemicals(file):
#     with open(file)as f:
#         lines = f.readlines()
#     elements = {
#         "AtomicNumber":[],
#         "Symbol":[],
#         "Name":[]
#     }
#     for element in lines:
#         element = element.split(" ")
#         elements["AtomicNumber"].append(element[0].strip())
#         elements["Symbol"].append(element[1].strip())
#         elements["Name"].append(element[2].strip())
#     return elements

# elements = getChemicals(fileLocation+"chemicals.txt")

# def getInfo(element:str):
#     global elements
#     try:
#         if element.isdigit():
#             ind = elements["AtomicNumber"].index(element)
#         elif len(element)<3:
#             ind = elements["Symbol"].index(element.lower().capitalize())
#         else:
#             ind = elements["Name"].index(element.lower().capitalize())
            
#         return f"AtomicNumber : {elements['AtomicNumber'][ind]}\n      Symbol : {elements['Symbol'][ind]}\n        Name : {elements['Name'][ind]}"
#     except:
#         return "Wrong element info enetered"


# while True:
#     el = input("Enter an element (AtomicNumber or Symbol or Name) to get info >>> ")
#     if el=="":
#         print("Bye 🧑🏿‍🤝‍🧑🏿")
#         break
#     print(getInfo(el))

### Exercise 162:A Book with No E...
# def getCleanWords(filename:str)->list:
#     punctuation = "[]{}|-!@#$%^&*()_+/*<>?~`':;,.\n"
#     with open(filename,"rt") as file:
#         f = file.readlines()
#     words = []
#         ### Getting all words
#     for line in f:
#         for mark in punctuation:
#             line = line.replace(mark,"")
#         line = line.split(" ")
#         nline = []
#         for i in line:
#             if i!='':
#                 nline.append(i)
#         words.extend(nline)
#     return words
        
# def getProportions(file):
#     letters = {chr(i):0 for i in range(65,91)}
#     words = getCleanWords(file)
#     print(f"There are {len(words)} words in the file")
#     for word in words:
#         while len(word)!=0:
#             if ord(word[0].upper())>=65 and ord(word[0].upper())<=90:
#                 letters[word[0].upper()]+=1
#                 word = word.replace(word[0],"")
#             else:
#                 word = word.replace(word[0],"")
#     return letters

# res = getProportions(fileLocation+"CoralReef.txt")
# print(res)
# vals = list(res.values())
# keys = list(res.keys())
# minval = min(vals)
# print("The rarest letter(s) in the file is(are):")
# for i in range(len(vals)):
#     if vals[i]==minval:
#         print(f"\t\t\t\t\t> {keys[i]} used in {vals[i]} words")      

# ### Exercise 163: Names that Reached Number One
# startYear = 2018
# endYear = 2021

# fileLocation = fileLocation + "163\\"

# def getCommon(startYear,endYear):
#     boys = []
#     girls = []
#     for fileyear in range(startYear,endYear+1):
#         with open(fileLocation+str(fileyear)+"Boys","rt") as bf:
#             name = bf.readline().split(" ")[0].strip()
#             if name not in boys:
#                 boys.append(name)
#         with open(fileLocation+str(fileyear)+"Girls","rt") as gf:
#             name = gf.readline().split(" ")[0].strip()
#             if girls not in girls:
#                 girls.append(name)
#     return {"Boys":boys,"Girls":girls}

# print(getCommon(startYear,endYear))
            
### Exercise 164:Gender Neutral Names
# startYear = 2018
# endYear = 2021

# fileLocation = fileLocation + "163\\"

# def getCommon(startYear,endYear):
#     boys = []
#     girls = []
#     common = []
#     for fileyear in range(startYear,endYear+1):
#         with open(fileLocation+str(fileyear)+"Boys","rt") as bf:
#             names = bf.readlines()
#             for i in range(len(names)):
#                 names[i] = names[i].split(" ")[0].strip()
#                 if names[i] not in boys:
#                     boys.append(names[i])
        
#         with open(fileLocation+str(fileyear)+"Girls","rt") as gf:
#             names = gf.readlines()
#             for i in range(len(names)):
#                 names[i] = names[i].split(" ")[0].strip()
#                 if names[i] not in girls:
#                     girls.append(names[i])
#     # print(boys)
#     for name in boys:
#         for gname in girls:
#             if name==gname:
#                 common.append(name)
#     return common

# print(getCommon(startYear,endYear))

### Exercise 165:Most Births in a given Time Period
# startYear = 2018
# endYear = 2021

# fileLocation = fileLocation + "163\\"

# def getCommon(startYear,endYear):
#     boymax = ["",0]
#     girlmax = ["",0]

#     for fileyear in range(startYear,endYear+1):
#         with open(fileLocation+str(fileyear)+"Boys","rt") as bf:
#             names = bf.readlines()
#         for i in range(len(names)):
#             names[i] = names[i].split(" ")
#             names[i][1] = int(names[i][1])
#             if names[i][1]>boymax[1]:
#                 boymax = names[i][:]
        
#         with open(fileLocation+str(fileyear)+"Girls","rt") as gf:
#             names = gf.readlines()
#         for i in range(len(names)):
#             names[i] = names[i].split(" ")
#             names[i][1] = int(names[i][1])
#             if names[i][1]>girlmax[1]:
#                 girlmax = names[i][:]
        
#     # print(boys)

#     return [boymax,girlmax]

# print(getCommon(startYear,endYear))

### Exercise 166: Distinct Names
# startYear = 2018
# endYear = 2021

# fileLocation = fileLocation + "163\\"

# def getCommon(startYear,endYear,gender):
#     boys = []
#     bdist = []
    
#     for fileyear in range(startYear,endYear+1):
#         with open(fileLocation+str(fileyear)+gender,"rt") as bf:
#             names = bf.readlines()
#         for name in names:
#             boys.append(name.split()[0])
    
#     for i in range(len(boys)):
#         b=True
#         for j in range(len(boys)):
#             if boys[i]==boys[j] and  i!=j:
#                 b=False
#                 break
#         if b:
#             bdist.append(boys[i])

#     return bdist

# print(getCommon(startYear,endYear,"Boys"),getCommon(startYear,endYear,"Girls"))

### Exercise 167: Spell Checker
def getCleanWords(text:str)->list:
    punctuation = "-!@#$%^&*()_+/*<>?~`:;,.\n"
    words = []
        ### Getting all words
    for mark in punctuation:
        text = text.replace(mark,"")
    text = text.split(" ")
    nline = []
    for i in text:
        if i!='':
            nline.append(i)
            
    words.extend(nline)
    return words
        
def getMissSpellings(text):
    with open(fileLocation+"wiki-100k.txt","rt",encoding="utf8") as wiki:
        words = {word.strip():0 for word in wiki.readlines()}
    textWords = getCleanWords(text)
    errors = []
    for i in textWords:
        try:
            a = words[i]
        except:
            errors.append(i)
    return errors

wrongs = getMissSpellings(input('Enter a text >>> '))
print(f"This(these) word(s) is(are) spelled in a wrong way {wrongs}" if wrongs!=[] else "Everything is correct" )
    

