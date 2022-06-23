# from ast import operator
# from optparse import Values


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


##### Book 136
# mydict = {
#     "a":5,
#     "b":6,
#     "c":18,
#     "f":5
# }

# srch = int(input("Enter the value to search >>> "))
# res = []
# for i in mydict:
#     if srch==mydict[i]:
#         res.append(i)

# print(res)


##### Book 137
# import random
# d = {}
# for i in range(1000):
#     d1 = int(random.randint(1,6))
#     d2 = int(random.randint(1,6))
#     sum = d1+d2
#     if sum in d:
#         d[sum] += 1
#     else: d[sum] = 1
# d2 = sorted(d)
# res = {}
# for i in d2:
#     res[i] = d[i]/1000*100
# print(res)

