#Slide
### Task No. 1 Calculator
### Task No. 2 Max
# def maxOf(a,b):
#     return a if a>b else b

# print(maxOf(5,25))
### Task No. 3 Sum of numbers
# def sum(*x):
#     s = 0
#     for i in x:
#         s+=i
#     return s

# print(sum(1,5,3,4))
### Task No. 4 Product of numbers
# def sum(*x):
#     s = 1
#     for i in x:
#         s*=i
#     return s

# print(sum(1,5,3,4))
### Task No. 5 Sum of numbers in string
# def sumOfNumbers(text):
#     s = 0
#     num = ""
#     for i in text:
#         if i.isdigit():
#             num+=i
#         if not i.isdigit() and num!="":
#             print(num)
#             s += int(num)
#             num = ""
#     return s

# inp = input("Enter a text >>> ")
# print(sumOfNumbers(inp))
### Task No. 6
# passengers = []
# def prepareForFlight():
#     global passengers
#     for i in range(0,3):
#         a = int(input("Enter the passengers age >>> "))
#         if a<16:
#             print("Too young!")
#             return
#         else:
#             passengers.append(a)
#     print("Get Ready!")
# prepareForFlight()
        
        


    
### Exercise 173:Total the Values
### Exercise 174: Greatest Common Divisor
