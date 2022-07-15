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

