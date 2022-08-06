###### Task 1 My version
## Input >>> bar(Text1)(word2)  Output >>> bar1txeT2drow
## Ipnut >>> bar(Text1(word2)) Output >>> bar(Text12drow) >>> barword21txeT
text = input("Enter text >>>> ")  
newt =""
def checkBrackets(txt):    
    global newt
    for i in range(0,len(txt)):
        if(txt[i]=="("):            
            st = i+1
            j=i
            while(txt[j]!=")"):                
                j+=1 
            newt=checkBrackets(txt[st:j+1]).replace("(","").replace(")","")[::-1]+newt
            
        else:continue
    return txt 

print(text)
newt = text
while newt.rfind("(")!=-1:
    open = newt.rfind("(")
    close = newt[open:len(newt)].find(")")+open
    newt = newt[0:open] + newt[open+1:close][::-1] + (newt[close+1:len(newt)] if close<len(newt) else "" )
    print(newt)

        
        

################# From GeeksForGeeks ################
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

