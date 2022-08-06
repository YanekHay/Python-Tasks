# list compression
# mylist = [i for i in range(15) if i%2 ==0]
# print(mylist)

####### Slides #######

### Task 13.1
# lst  = [1,5,3,52,(1,5,3,"bar",'a'),12,0,94]

# q=0
# for i in lst:
#     print(type(i))
#     if type(i) is tuple:
#         break
#     q+=1

# print(q)     
### Task 13.2
# tup = (5,1,2,"add","what","sun",1.2,195)
# tup = tup[::-1]
# print(tup)
### Task 13.3
# tup = (5,1,2,"add","what","sun",1.2,195)
# print(len(tup))
### Task 13.4
# tup = (5,1,2,"add","what","sun",1.2,195)
# text = "".join(str(tup))
# print (text) 
### Task 13.5
# tup = (5,1,2,1.2,195)
# s = 0
# for i in tup:
#     s+=i
# print(s)
### Task 13.6
# tup = (5,1,2,"add","what","sun",1.2,195)
# for i in tup:
#     if type(i) is str :
#         print(i)

### Task 14.1
# lst = [1,5,1,32,23,8200,8,1]
# s = 0
# for i in lst:
#     s+=i
# print(s)
### Task 14.2
# lst = [1,5,1,32,23,10,8,1]
# p=1
# for i in lst:
#     p*=i
# print(p)
### Task 14.3
# lst = [1,5,1,32,23,10,8,1]
# lst.sort()
# print(lst[-1])
### Task 14.4
# list1 = [1,5,1,32,23,10,8,1]
# list2 = [99,56,4,98,316,2,89,12]

# b= False
# for i in list1:
#     if i in list2:
#         b=True        
#         break

# print("Lists have common members" if b else "Lists have nothing in common")


