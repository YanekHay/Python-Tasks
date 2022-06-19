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

## կա շախմատի տախտակ, պետքա ասի որ սյան ու տողի վրա պետքա թագուհին դրվի




# Calculator
inp = input("Enter an expression >>> ")
operators = "+-*/^%"
unary = "+-"
#Remove spaces
inp = inp.replace(" ","")

inFixExpression = []
token = ""
print(inp)

## Tokenizing a string 
for i in inp:    
    if i in operators:
        if token!="":
            inFixExpression.append(token)
        inFixExpression.append(i)
        token = ""
        continue        
    token = f"{token}{i}"    
inFixExpression.append(token)   
print(inFixExpression)

## Finding unar operators
print("".join(inFixExpression))
if(inFixExpression[0] in unary):
    inFixExpression[0] = "u" + inFixExpression[0]
    
for i in range(1,len(inFixExpression)):
    if (inFixExpression[i-1] in operators) and (inFixExpression[i] in unary):
        inFixExpression[i] = "u" + inFixExpression[i]
print(inFixExpression)

#get left num
summary = 0
for i in range(len(inFixExpression)):
    if(inFixExpression[i].isdigit):
        num = int(inFixExpression[i]) if(i==0 or inFixExpression[i-1]=="u+") else -int(inFixExpression[i])
        print(num)
# leftNum = 