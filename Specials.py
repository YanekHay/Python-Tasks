####### Task 1
### Input >>> bar(Text1)(word2)  Output >>> bar1txeT2drow
### Ipnut >>> bar(Text1(word2)) Output >>> bar(Text12drow) >>> barword21txeT
# def func(text):
#     if text.find("(")==-1:
#         return text.replace()
#     else:
#         return n*func(n-1)

# print(func(5))

# text = input("Enter text >>>> ")  
# newt =""
# def checkBrackets(txt):    
#     global newt
#     for i in range(0,len(txt)):
#         if(txt[i]=="("):            
#             st = i+1
#             j=i
#             while(txt[j]!=")"):                
#                 j+=1 
#             newt=checkBrackets(txt[st:j+1]).replace("(","").replace(")","")[::-1]+newt
            
#         else:continue
#     return txt 
        
#             #

# print (t)
# print(checkBrackets(text))
# print(newt)
            

# text = input("Enter text >>>> ")  
# print(text)
# newt = text
# while newt.rfind("(")!=-1:
#     open = newt.rfind("(")
#     close = newt[open:len(newt)].find(")")+open
#     newt = newt[0:open] + newt[open+1:close][::-1] + (newt[close+1:len(newt)] if close<len(newt) else "" )
#     print(newt)

        
        

################## From GeeksForGeeks ################
# def reverseParentheses(strr, lenn):
#     st = []
 
#     for i in range(lenn):
 
#         # Push the index of the current
#         # opening bracket
#         if (strr[i] == '('):
#             st.append(i)
 
#         # Reverse the substring starting
#         # after the last encountered opening
#         # bracket till the current character
#         elif (strr[i] == ')'):
#             temp = strr[st[-1]:i + 1]
#             strr = strr[:st[-1]] + temp[::-1] + \
#                    strr[i + 1:]
#             del st[-1]
 
#     # To store the modified string
#     res = ""
#     for i in range(lenn):
#         if (strr[i] != ')' and strr[i] != '('):
#             res += (strr[i])
#     return res
 
# # Driver code
# if __name__ == '__main__':
#     strr = input(">>>  ")
#     lenn = len(strr)
#     st = [i for i in strr]
 
#     print(reverseParentheses(strr, lenn))
 










# for i in range(0,len(text)):
#     if(text[i]=="("):
#         print(i)

## մուտք կամայական թիվ, եթե ստացվումա եռանկյուն՝՝ 15, 21, 
# 0 
# 1 0
# 2 6 00
# 3 7 10 00
# 4 8 11 13 00
# 5 9 12 14 15 00

#Correct numbers are 1, 3, 6, 10, 15, 21, 28, 36, ...

# n = int(input("Enter a number >>> "))
# correctNum = 1
# step=1
# while(abs(correctNum-n)>step):
#     correctNum+=step+1
#     step+=1

# print(f"Num: {correctNum}\nStep: {step}")
# output = ""
# for i in range(1,step+1):
#     output =f"{output}{i:<3}"   
#     val = i+step-1
#     for j in range(i-1):
#         output= f"{output} {val:<3}"
#         val+=step-j-2
#     output=f"{output}\n"

# print(output)

    


####  12 բիլիարդի գնդակ, 1-ը բռակ։ Նժարավոր կշեռքով 3 քայլով ասել որն է բռակ
####V1.0    6/6 ---> 3/3 -----> 1/1 and 1 left
####V2.0    3/3 if not ---> another 3/3 ---> 1/1 and 1 left


#### Are the brackets opened and closed right
#  ( { * [] * } )

# openers = "({["
# closers = ")}]"
# text = input("Enter a text >>> ")
# indexes = ""
# print(text.count("(")  )
# for i in range(len(text)):
#     for j in range(len(openers)):    
#         if(text[i]==openers[j] or text[i]==closers[j]):
#             indexes = f"{indexes}{text[i]}{i}"
            
#     print(q)        
  

# print(indexes)    


# Calculator
# inp = input("Enter an expression >>> ")
# operators = "+-*/^%"
# unary = "+-"
# #Remove spaces
# inp = inp.replace(" ","")

# inFixExpression = []
# token = ""
# print(inp)

# ## Tokenizing a string 
# for i in inp:    
#     if i in operators:
#         if token!="":
#             inFixExpression.append(token)
#         inFixExpression.append(i)
#         token = ""
#         continue        
#     token = f"{token}{i}"    
# inFixExpression.append(token)   
# print(inFixExpression)

# ## Finding unar operators
# print("".join(inFixExpression))
# if(inFixExpression[0] in unary):
#     inFixExpression[0] = "u" + inFixExpression[0]
    
# for i in range(1,len(inFixExpression)):
#     if (inFixExpression[i-1] in operators) and (inFixExpression[i] in unary):
#         inFixExpression[i] = "u" + inFixExpression[i]
# print(inFixExpression)

# #get left num
# summary = 0
# for i in range(len(inFixExpression)):
#     if(inFixExpression[i].isdigit):
#         num = int(inFixExpression[i]) if(i==0 or inFixExpression[i-1]=="u+") else -int(inFixExpression[i])
#         print(num)
# # leftNum = 
######################   QUEENS   ######################
## կա շախմատի տախտակ, պետքա ասի որ սյան ու տողի վրա պետքա թագուհին դրվի

# def printTable(chess):
#     for i in range(0,len(chess)):
#         print()
#         for j in range(0,len(chess[i])):
#             print(f" {chess[i][j]:<3} ",end="")
#     print()
            
# def placeQueen(posX,posY,num):    
#     for i in range(0,8):
#         for j in range(0,8):
#             if i == posX and j == posY:
#                 chesstable[i][j] = f"Q{num}"
#             elif (i+j == (posX+posY) or posX == i or posY == j or i-j == posX-posY) and chesstable[i][j]==0 :
#                 chesstable[i][j] = 1

# chesstable = []
# leftCoords = []
# queenCount = 0

# def printTable(chess):
#     for i in range(0,len(chess)):
#         print(f" {chr(int(chess[i][0])+97)+str(int(chess[i][-1])+1):<3} ",end="")
#     print("\n\n")
  
# def placeQueen(posX,posY):
#     global queenCount,leftCoords,floors
#     if len(leftCoords) ==0:
#         return leftCoords
#     queenCount+=1
#     newCoords = []   
#     printTable(leftCoords) 
#     for i in range(0,len(leftCoords)):
#             row = int(leftCoords[i][0])
#             col = int(leftCoords[i][-1])
#             if not ((row == posX and col == posY) or ((row+col == (posX+posY) or posX == row or posY == col or row-col == posX-posY))):
#                newCoords.append(leftCoords[i])
#     layers.append(newCoords)        
#     #print(newCoords[0][0],newCoords[0][-1])
#     #leftCoords = placeQueen(int(newCoords[0][0]),int(newCoords[0][-1]))
       
#     leftCoords = newCoords
#     for i in range(len(newCoords)):
#         return placeQueen(int(newCoords[i][0]),int(newCoords[0][-1]))
    


                
# chesstable = []

# for i in range(0,8):
#     for j in range(0,8):
#         chesstable.append(f"{i}:{j}")

# leftCoords = chesstable
# #printTable(chesstable)
# a = placeQueen(5,4)
# q = 1
# print(floors)
# print("\n\n")
# print(queenCount)        

###############################
#կնոպկով հեռախոսի խնդիրը 
# buttons = {
#     '1':"",
#     '2':"ABC",
#     '3':"DEF",
#     '4':"GHI",
#     '5':"JKL",
#     '6':"MNO",
#     '7':"PQRS",
#     '8':"TUV",
#     '9':"WXYZ",
#     '0':" ",
#     '*':"*+",
#     "#":"#"    
# }


# inp = input("Enter the digits >>> ")
# depth = len(inp)

# counters = [0 for i in range(0,depth)]

# def loopRecursion(level):
#     global counters
#     if level == depth:
#         generateVariant()
#     else:
#         for counter in range(len(buttons[inp[level]])):
#             counters[level] = counter
#             loopRecursion(level+1)

# def generateVariant():
#     global inp,counters
#     variant = ""
#     i=0
#     for level in counters:        
#         variant += buttons[inp[i]][level]
#         i+=1
#     print(variant)
            
    
# loopRecursion(0)

# print(round(0.299238 * (int(inp)*3+64) - 17.763365)+63)\
    
# The longest prefix

# strs = ["reflower","flow","flight"]

# strs.sort(key=len)
# print(strs)
# pref = strs[0].lower()


# for i in range(0,len(strs)+1): 
#     b=True
#     for j in range(1,len(strs)):         
#         if pref != strs[j][:len(pref)].lower():
#             print(strs[j][:len(pref)].lower(),pref)
#             b=False
#             break
#     if b==False:
#         print(len(pref))
#         pref = pref[:len(pref)-1] if len(pref)>1 else ""
        
# print(pref)    

# LeetCode 33. Search in Rotated Sorted Array
# nums = [4,5,6,7,0,1,2,8]
# target = 0
# correct = []

# if target in nums:
#     correct = nums[nums.index(target):]
#     print(nums[nums.index(target):])
#     correct.extend(nums[:nums.index(target)])
#     sorted = correct[:]
#     sorted.sort()
#     print(sorted)
#     if sorted==correct:
#         print(nums.index(target))
#     else:
#         print(-1)
# else:
#     print(-1)
    
        

# Leetcode 8. String to Integer

# class Solution:
#     def myAtoi(s: str) -> int:
#         startInd = -1
#         letters = "abcdefghijklmnopqrstuvwxyz."
#         for i in range(len(s)):
#             if s[i].isdigit():
#                 startInd = i
#                 break
#         if startInd>=0:
#             for i in range(0,startInd):
#                 if s[i] in letters:
#                     return(0)
#             number = ""
#             if startInd>0 and (s[startInd-1]=="-" or  s[startInd-1]=="+")  :
#                 if startInd>1 and (s[startInd-2]=="-" or  s[startInd-2]=="+"):
#                     return 0
#                 else:
#                     number+=s[startInd-1]
#             elif not("+" in s[:startInd] or "-" in s[:startInd]):
#                 number = ""
#             else:
#                 return 0
#             while startInd<len(s) and s[startInd].isdigit():
                
#                 number+=s[startInd]
#                 startInd+=1
#             number = int(number)
#             if number>2**31-1:
#                 return 2**31-1
#             elif number<-(2**31):
#                 return -(2**31)
#             else:
#                 return(number)
#         else:
#             return(0)
        

# print(Solution.myAtoi(input("Enter a text >>> ")))

#LeetCode 31. Next Permutation
# arr = [1,2,3]
# out = arr[:]
# sortedDesc = arr[:]
# sortedDesc.sort(reverse=True)
# if sorted == arr:
#     print(arr)
# else:
#     while int("".join(out)) < int("".join(out)):
#         for i in range(len(out)):

# nums = [2,3,4,5,6,8,7,9,80,11,9,15,69]
# arr =  [1,5,6,4,5,5,5]
# cpy = arr[:]

# num = 0
# for i in arr:
#     num = num*10+i
# print(num)
    
# ### Getting all numbers
# numbers = []
# i=len(arr)-1
# it = 0
# while True:
    
#     arrStr = []
#     for j in arr:
#         arrStr.append(str(j))    
#     c = arr[i]
#     arr[i] = arr[i-1]
#     arr[i-1] = c
#     numbers.append(int("".join(arrStr)))
#     if arr==cpy and it>=1:
#         break
#     if i>(1-len(arr)):
#         i = (i-1)
        
#     else:
#         it+=1
#         i=len(arr)-1
    

# myset = set(numbers)
# print(myset.get)
# print (myset)
# print(myset[(numbers.index(num)+1)%len(myset)])


# 01111011      123 9
# 10000100      132 81
# 11010101      213 18
# 11100111      231 81
# 000100111000  312 9
# 000101000001  321
#1234 9  
#1243 81
#1324 18
#1342 81
#1423 9
#1432 711
#2134 9
#2143 171
#2314 27
#2341


# list = [1,3,2]

# class Solution:
#     def nextPermutation(nums)->None:
#         pointer=0
#         length=len(nums)
#         if length<=2:
#             return nums.reverse()
#         pointer=length-2
#         while(pointer>=0 and nums[pointer]>=nums[pointer+1]):
#             pointer-=1
#         if pointer==-1:
#             return nums.reverse()
#         for i in range(length-1,pointer,-1):
#             if nums[pointer]<nums[i]:
#                 nums[pointer],nums[i]=nums[i],nums[pointer]
#                 break

#         nums[pointer+1:]=reversed( nums[pointer+1:])
#         print(nums)
# Solution.nextPermutation(list)

#### Print all possible permulations of this list
# myList = [1,2,5,6,5]
# arr = myList[:]
# arr.sort()

# depth = len(arr)
# q = 0

# def loop(level,res,arr):
#     global depth,q
#     if level == depth:
#         q+=1
#         print(res)
#         return
#     else:
#         for i in range(len(arr)):
#             cpy = arr[:]
#             cpy.remove(arr[i])
#             res.append(str(arr[i]))
#             loop(level+1,res,cpy) 
            
#             del res[-1]
            

# loop(0,[],arr)
# print(f"\n\nThere are {q} permulations of {myList}")

#### Binary search
# def find(num,arr,start,end):
#     mid = (end+start)//2
#     if arr[mid]==num:
#         return mid
#     elif arr[mid]>num:
#         return find(num,arr,start,mid-1)
#     elif arr[mid]<num:
#         return find(num,arr,mid+1,end)
    

# arr = [12,52,0,5,1,6544,21]
# start = 0
# end = len(arr)

# num = int(input("Enter a number to search >>> "))
# arr.sort()
# print(arr)
# print(find(num,arr,start,end))
print("Why is not working?")
print("This is a Test")