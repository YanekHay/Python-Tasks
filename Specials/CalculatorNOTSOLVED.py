
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
