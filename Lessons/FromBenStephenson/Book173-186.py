### Exercise 173:Total the Values
# total = 0
# def readValues():
#     global total
#     inp = input("Enter a number >>> ")
#     if inp == "":
#         print(f"The sum of your inputs is ->->-> {total}")
#         return
#     else:
#         total+=int(inp)
#         readValues()

# readValues()
### Exercise 174: Greatest Common Divisor
# def findDivisor(a,b):
#     if b == 0:
#         return a
#     else:
#         c = a%b
#         return findDivisor(b,c)

# print(findDivisor(0,0))

### Exercise 175: Recursive Decimal to Binary
# def decTobin(num,res):
#     if num==0:
#         return (res+'0')[::-1]
#     elif num==1:
#         return (res+'1')[::-1]
#     else:
#         res+=str(num%2)
#         return decTobin(num//2,res)

# print(decTobin(156,""))
        
### Exercise 176:The NATO Phonetic Alphabet
# def makeWord(NATOexpr:str,res) -> str:
#     if NATOexpr.find(" ")==-1:
#         return res+NATOexpr[0]    
#     else:
#         res+=NATOexpr[0]
#         # print(res)
#         return makeWord(NATOexpr[NATOexpr.find(" ")+1:],res)

# print(makeWord("Hotel Echo Lima Lima Oscar",""))

### Exercise 177: Roman Numerals
# numerals = {
#     'M' : 1000,
#     'D' : 500,
#     'C' : 100,
#     'L' : 50,
#     'X' : 10,
#     'V' : 5,
#     'I' : 1,
# }
# def romToInt(roman,sum,lvl):   
#     global numerals
#     if lvl==len(roman)-1:
        
#         return sum+numerals[roman[lvl]]
#     else:
#         sum+= numerals[roman[lvl]] if (numerals[roman[lvl]] >= numerals[roman[lvl+1]]) else -numerals[roman[lvl]]
#         return romToInt(roman,sum,lvl+1)

# print(romToInt(input("Enter a roman number >>> ").upper(),0,0))
        
### Exercise 178: Recursive Palindrome
# def isPalindrome(text:str):
#     if len(text) == 0 or len(text) == 1:
#         return True
#     else:
#         if text[0]==text[-1]:
#             return isPalindrome(text[1:-1])
#         else:
#             return False
# while True:
#     print(isPalindrome(input(">>> ")))

### Exercise 179: Recursive Square Root
# def sqRoot(num,guess):
#     if abs(guess*guess-num)<num*(10**-12):
#         return guess
#     else:
#         return sqRoot(num,(guess+(num/guess))/2)

# print(sqRoot(float(input("Enter a number >>> ")),1))
        
### Exercise 180: String Edit Distance
# def editDist(text1,text2):
#     if len(text1)==0:
#         return len(text2)
#     elif len(text2)==0:
#         return len(text1)
#     else:
#         cost = 0
#         if text1[-1]!=text2[-1]:
#             cost = 1
#         d1 = editDist(text1[0:-1],text2)+1
#         d2 = editDist(text1,text2[0:-1])+1
#         d3 = editDist(text1[0:-1],text2[0:-1])+cost
#         return min(d1,d2,d3)
# print(editDist("kitten","sitting"))


### Exercise 181: Possible Change 
## 1 Nickel is  (5/100) $
## 1 Dime is    (10/100)$
## 1 Quarter is (25/100)$
## coins = {0.05:"Nickel",
##          0.1:"Dime",
##          0.25:"Quarter"}


# results = []
# res = []

# def findway(total,d):
#     global results,res,count
    
#     if total == 0:
#         if (len(res)==count):     
#                 results.append(res)
#         return
#     elif total <0:
#         res=[]
#         return 
#     else:
#         if (round(total/0.25)==count-d or round((total-0.25)/0.1)+d+1>=count or round((total-0.25)/0.05)+d+1>=count) and ((d>0 and res[d-1]==0.25) or d==0) and total-0.25>= 0:
#             res.append(0.25)
#             findway(round(total-0.25,8),d+1)
            
#         # print(round((total/0.1)),round((total-0.1)/0.05),count-d)

#         if (round(total/0.1)==count-d or round((total-0.1)/0.05)+d+1>=count) and ((d>0 and res[d-1]>=0.1) or d==0) and total-0.1 >= 0:
#             if d==0:
#                 res = []
#             else:
#                 res = res[:d]
#             res.append(0.1)
#             findway(round(total-0.1,8),d+1)
#         # print(round(total/0.05),count-d)
#         if  round(total/0.05)==count-d and ((d>0 and res[d-1]>=0.05) or len(res)==0) and total-0.05 >= 0:
#             if d==0:
#                 res = []
#             else:
#                 res = res[:d]

#             res.append(0.05)
#             findway(round(total-0.05,8),d+1)

# count = 102
# money = 5
# findway(money,0)
# for i in range(len(results)):
#     print (f"{i}.\n\tQuarter: {results[i].count(0.25)}\n\tDime: {results[i].count(0.1)}\n\tNickel: {results[i].count(0.05)}\n")

### Exercise 182: Spelling with Element Symbols
## import periodictable
# import mendeleev

# elements = {}

# for i in mendeleev.elements.get_all_elements():
#     elements[i.symbol.lower()] = i.name


# print(elements)

# def spellStart(name,spelled = ''):
#     global elements
#     if name=="":
#         return spelled
#     else:
#         if name[:2] in elements.keys():
#             return spellStart(name[2:],spelled+elements[name[:2]]+" ")
#         elif name[0] in elements.keys():
#             return spellStart(name[1:],spelled+elements[name[0]]+" ")
#         else:
#             return "Can not be spelled!"

# def spellStart1(name,spelled = ''):
#     global elements
#     if name=="":
#         return spelled
#     else:
#         if name[0] in elements.keys():
#             return spellStart(name[1:],spelled+elements[name[0]]+" ")
#         elif name[:2] in elements.keys():
#             return spellStart(name[2:],spelled+elements[name[:2]]+" ")
#         else:
#             return "Can not be spelled!"

# res = set()

# qStart = 0
# qEnd = 0
# qStart1 = 0
# qEnd1 = 0
# for i in elements:
#     if spellStart(elements[i].lower(),"")!="Can not be spelled!":
#         qStart+=1
#         print("From start ---:::1) ",elements[i],"  ",spellStart(elements[i].lower(),""))
#         res.add(elements[i])
#     if spellStart1(elements[i].lower(),"")!="Can not be spelled!":
#         qStart+=1
#         print("From start ---:::2) ",elements[i],"  ",spellStart1(elements[i].lower(),""))
#         res.add(elements[i])
#     if spellStart(elements[i].lower()[::-1],"")!="Can not be spelled!":
#         qEnd+=1
#         print("From end  +++:::1) ", elements[i],"  ",spellStart(elements[i].lower(),""))
#         res.add(elements[i])
#     if spellStart1(elements[i].lower()[::-1],"")!="Can not be spelled!":
#         qStart+=1
#         print("From end +++:::2) ",elements[i],"  ",spellStart1(elements[i].lower(),""))
#         res.add(elements[i])
        
# print(f"\nTotal {qStart} element names can be spelled with element symbols from start")
# print(f"\nTotal {qEnd} element names can be spelled with element symbols from end")
# print(res)
# print(len(res))
## Exercise 183: Element Sequences
# import mendeleev
# ######### With Dictionary 
# elementNames = {}
# for i in  mendeleev.elements.get_all_elements():
#     el = i.name.lower()
#     if el[0] in elementNames.keys():
#         elementNames[el[0]].append(el)
#     else:
#         elementNames[el[0]] = [el]
        
# maxchain=[]
# def makechain(chain:list[str],elnames:dict = elementNames):
#     global maxchain
#     elnames[chain[-1][0]].remove(chain[-1])
#     if len(elnames[chain[-1][0]])==0 or len(elnames[chain[-1][-1]])==0:
#         if len(maxchain)<len(chain):
#             maxchain = chain[:]
#     else:
#         for i in range(len(elnames[chain[-1][-1]])):
#             if len(elnames[chain[-1][-1]])!=0:
#                 chain.append(elnames[chain[-1][-1]][0])
#                 makechain(chain,elnames)
#                 del chain[-1]

# while True:
#     first = input("Enter a chemical element >>> ").lower()
#     if first in elementNames[first[0]]:
#         makechain([first],elementNames)
#         break
#     else:
#         print("Wrong input, try again: \n")
  
# print(maxchain,len(maxchain))


### Exercise 184: Flatten a List
# def flatten(a:any, mylist:list[any]) -> list[any]:
#     if a == []:
#         return mylist
#     else:
#         if not isinstance(a[0], list):
#             mylist.append(a[0])
#             a.remove(a[0])
#             return flatten(a, mylist)
#         else:
#             mylist.extend(flatten(a[0], []))
#             a.remove(a[0])
#             return flatten(a, mylist)
# print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]], []))

### | Exercise 185: Run-Length Decoding
### | Exercise 186: Run-Length Encoding
### V #################################
# def encode(text,res:list = []):
#     if len(text)==0:
#         return res
#     elif text[0] not in res:
#         res.append(text[0])
#         res.append(1)
#     else:
#         res[res.index(text[0])+1]+=1
#     res = encode(text[1:],res)
#     return res

# def decode(encoded:list,res:list = []):
#     if len(encoded)==0:
#         return res
#     else:
#         for i in range(encoded[1]):
#             res.append(encoded[0])
#         res = decode(encoded[2:] if len(encoded)>2 else [])
#         return res
# encoded = input("Enter a text >>> ")
# encoded = encode(encoded)
# print(f"Your text encoded    ---> {encoded}")
# print(f"The encoding decoded ---> {decode(encoded)}")
# print("abac"[0:0])