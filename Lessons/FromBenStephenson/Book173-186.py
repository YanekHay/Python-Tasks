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

### Exercise 182: Spelling with Element Symbols
## import periodictable
import mendeleev

elements = {}

for i in mendeleev.elements.get_all_elements():
    elements[i.symbol.lower()] = i.name


print(elements)

def spellStart(name,spelled):
    global elements
    if name=="":
        return spelled
    else:
        if name[:2] in elements.keys():
            return spellStart(name[2:],spelled+elements[name[:2]]+" ")
        elif name[0] in elements.keys():
            return spellStart(name[1:],spelled+elements[name[0]]+" ")
        else:
            return "Can not be spelled!"

def spellStart1(name,spelled):
    global elements
    if name=="":
        return spelled
    else:
        if name[0] in elements.keys():
            return spellStart(name[1:],spelled+elements[name[0]]+" ")
        elif name[:2] in elements.keys():
            return spellStart(name[2:],spelled+elements[name[:2]]+" ")
        else:
            return "Can not be spelled!"

# def spellEnd(name,spelled):
#     global elements
#     if name=="":
#         return spelled
#     else:
#         if name[-2:] in elements.keys():
#             return spellEnd(name[:-2],elements[name[-2:]]+" "+spelled)
#         elif name[-1] in elements.keys():
#             return spellEnd(name[:-1],elements[name[-1]]+" "+spelled)
#         else:
#             return "Can not be spelled!"

res = set()

qStart = 0
qEnd = 0
qStart1 = 0
qEnd1 = 0
for i in elements:
    if spellStart(elements[i].lower(),"")!="Can not be spelled!":
        qStart+=1
        print("From start ---:::1) ",elements[i],"  ",spellStart(elements[i].lower(),""))
        res.add(elements[i])
    if spellStart1(elements[i].lower(),"")!="Can not be spelled!":
        qStart+=1
        print("From start ---:::2) ",elements[i],"  ",spellStart1(elements[i].lower(),""))
        res.add(elements[i])
    if spellStart(elements[i].lower()[::-1],"")!="Can not be spelled!":
        qEnd+=1
        print("From end  +++:::1) ", elements[i],"  ",spellStart(elements[i].lower(),""))
        res.add(elements[i])
    if spellStart1(elements[i].lower()[::-1],"")!="Can not be spelled!":
        qStart+=1
        print("From end +++:::2) ",elements[i],"  ",spellStart1(elements[i].lower(),""))
        res.add(elements[i])
        
print(f"\nTotal {qStart} element names can be spelled with element symbols from start")
print(f"\nTotal {qEnd} element names can be spelled with element symbols from end")
print(res)
print(len(res))
### Exercise 183: Element Sequences
# import mendeleev
# elementNames = []
# for i in  mendeleev.elements.get_all_elements():
#     elementNames.append(i.name.lower())

# print(elementNames)


# def findSequence(res):
    
### Exercise 184: Flatten a List

### Exercise 185: Run-Length Decoding
