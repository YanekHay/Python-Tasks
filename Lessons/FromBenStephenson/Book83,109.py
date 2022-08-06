### Exercise 85: Compute the Hypotenuse
# from math import sqrt

# def hypo(a,b):
#     return float(sqrt(a*a+b*b))

# a = float(input("a = "))
# b = float(input("b = "))
# print(hypo(a,b))

### Exercise 86: Taxi Fare
# def fare(dist):
#     return dist/140*0.25+4
# dist = float(input("Enter the distance traveled >>> "))
# print(fare(dist))

### Exercise 87: Shipping Calculator
# def calc(count):
#     return (count-1)*2.95+10.95
# count = float(input("How many items are there? >>> "))
# print(calc(count))
### Exercise 88: Median of Three Values
# from math import floor


# def median(values):
#     return values[floor(len(values)/2)] if len(values)%2==1 else (values[round(len(values)/2)-1]+values[round(len(values)/2)])/2
# values = []
# while True:
#     value = input("Enter a number >>> ")
#     if value =="":
#         break
#     values.append(float(value))

# print(f"The median is: {median(values)})

### Exercise 90: The Twelve Days of Christmas
# def sing(presents):
#     keys = list(presents.keys())
#     for day in range(len(keys)):
#         pr = ""
#         for i in range(day,-1,-1):
#             pr = f"{pr}\n{'And ' if  i==0 else ''}{presents[keys[i]]},"
#         print(f"On the {keys[day]} day of Christmas\nmy true love sent to me:{pr}.\n")

# presents = {
#     "first": "A partridge in a pear tree",
#     "second":"Two turtle doves",
#     "third":"Three french hens",
#     "fourth":"Four calling birds",
#     "fifth":"Five golden rings",
#     "sixth":"Six geese-a-laying",
#     "seventh":"Seven Swans-a-Swimming",
#     "eighth":"Eight Maids-a-Milking",
#     "ninth":"Nine Ladies Dancing",
#     "tenth":"Ten Lords-a-Leaping",
#     "eleventh":"Eleven Pipers Piping",
#     "twelfth":"Twelve Drummers Drumming",
# }

# sing(presents)

### Exercise 91: Gregorian Date to Ordinal Date
# def ordinalDate(day,month,year):
#     long = [1,3,5,7,8,10,12]
#     for i in range(1,month):
#         if i in long:
#             day +=31
#         elif i==2:
#             day += 28 if year%4!=1 else 29    
#         else:
#             day +=30   
#     return day

# print (ordinalDate(5,3,2022))       

### Exercise 92: Ordinal Date to Gregorian Date

# def grigoreanDate(day,year):
#     long = [1,3,5,7,8,10,12]
#     month = 1
#     while day>31:
#         if month in long:
#             day-=31
#         elif month==2:
#             day-=28 if year%4!=0 else 29
#         else:
#             day-=30
#         month+=1
#     return f"{day:02d}/{month:02d}/{year}"    
# print(grigoreanDate(64,2022))

### Exercise 93: Center a String in the TerminalWindow
from math import factorial


def center(text,windowWidth):
    if len(text)>=windowWidth:
        return text
    text = f"{' '*((windowWidth-len(text))//2)}{text}"
    text = f"{text}{' '* (windowWidth-len(text))}"
    return text 

# width = 30
# text = input("Enter a text >>> ")
# print(f"{'*'*width}\n{center(text,width)}")

### Exercise 94: Is It a Valid Triangle?
# def isValidTriangle(a,b,c):
#     l = [a,b,c]
#     l.sort(reverse=True)
#     if l[0]>(l[1]+l[2]):
#         return False
#     return True

# print(f'{"The given triangle is valid" if isValidTriangle(3,4,50) else "The given triangle is not valid"}')

### Exercise 95: Capitalize It
# def changeChar(text:str,char,pos):
#     res =""
#     for i in range(len(text)):
#         if i!=pos:
#             res +=text[i]
#         else:
#             res +=char
#     return res
       
# def Capitalize(text:str):
#     text = text.strip()
#     text = changeChar(text,text[0].upper(),0)
#     for i in ".!?":
#        text = text.replace(i,i + " ")
#     words = text.split(" ")
#     res = ""
#     for i in range(len(words)):
#         if words[i]!="":
#             if words[i][0]=="i":
#                 if len(words[i])>1 and words[i][1] in "'.,?":
#                     words[i] = changeChar(words[i],"I",0)
#                 elif len(words[i])==1:
#                     words[i] = "I"
#             elif i>0 and words[i-1]!="" and words[i-1][len(words[i-1])-1] in "!?.":
#                 print(words[i-1])
#                 words[i] = changeChar(words[i],words[i][0].upper(),0)
#             elif len(words[i])>1 and words[i][0] in "!?.":
#                 words[i] = changeChar(words[i],words[i][1].upper(),1)
#             res+=words[i] + " "

#     return res   

# l = "word is a    sword.am i right?"

# print(Capitalize(l))

### Exercise 96: Does a String Represent an Integer?
# def isInteger(text):
#     for i in range(1 if text[0] in "+-" else 0,len(text)):
#         if not text[i].isdigit():
#             return False
#     return True
# print(isInteger("-12"))

### Exercise 97: Operator Precedence
# def precedence(text:str):
#     operators = {
#         1:"+-",
#         2:"*/",
#         3:"^"
#     }
#     for key in operators:
#         for op in operators[key]:
#             if op in text:
#                 return key
#     return -1
# text = input("Enter a text >>> ")
# print(precedence(text))

### | Exercise 98: Is a Number Prime?
### | Exercise 99: Next Prime
### V

# from math import sqrt
# def isPrime(num:int):
#     if num<=2:
#         return False    
    
#     for i in range(2,round(sqrt(num))):
#         if num%i==0:
#             return False
#     return True

# num = int(input("Enter a number >>> "))
# print(isPrime(num))

# def nextPrime(num):
#     n = round(num)
#     while not isPrime(n):
#         n+=1
#     return n

# print(nextPrime(num))




### Exercise 101: Random License Plate
# def generatePlate():
#     import random
#     lic = ""
#     for i in range(0,4):
#         lic+= str(random.randint(0,9))
#     for i in range(0,3):
#         lic+= chr(random.randint(65,90))
#     return lic

# print(generatePlate())
### | Exercise 100: Random Password         ||||||
### | Exercise 102: Check a Password        ||||||
### | Exercise 103: Random Good Password    ||||||
### V                                       VVVVVV
# import random
# def generatePassword():
#     length = random.randint(7,10)
#     password = ""
#     for i in range(length):
#       password+=chr(random.randint(33,126))
#     return password  

# print(generatePassword())

# def isStrong(password):
#     if len(password)>=8:
#         hasUpper = False
#         hasLower = False
#         hasNumber = False
#         for i in password:
#             if i.isupper():
#                 hasUpper = True
#             elif i.islower():
#                 hasLower = True
#             elif i.isdigit():
#                 hasNumber = True
#             if hasUpper and hasLower and hasNumber:
#                 return True
#     return False

# def getGoodPassword():
#     steps = 1
#     while True:
#         p = generatePassword()
#         if isStrong(p):
#             print(f"{steps} passwords were generated to get a strong one")
#             return p
#         steps+=1
        
# password = "StrongPassword9"           
# print(getGoodPassword())

### Exercise 104: Hexadecimal and Decimal Digits
# def intTohex(num:int):
#     dict = {
#         i:str(i) for i in range(0,10) 
#     }
#     dict[10] = "A"
#     dict[11] = "B"
#     dict[12] = "C"
#     dict[13] = "D"
#     dict[14] = "E"
#     dict[15] = "F"
#     res = ""
#     while num!=0:
#         res+=dict[num%16]
#         num = num//16
#     return res[::-1]

# def hexToint(num:str):
#     dict = {
#         i:str(i) for i in range(0,10) 
#     }
#     dict[10] = "A"
#     dict[11] = "B"
#     dict[12] = "C"
#     dict[13] = "D"
#     dict[14] = "E"
#     dict[15] = "F"   
#     newDict = {}
#     for key in dict:
#         newDict[dict[key]] = key
#     res = 0
#     for i in num:
#         res=res*16+newDict[i]
#     return res


# print("Int to Hex :",intTohex(int(input("Enter a decimal number >>> "))),"\n")
# print ("Hex to Int :",hexToint(input("Enter a Hex number >>> ")))      
    
### Exercise 105: Arbitrary Base Conversions
# def convert(num:str,fromBase:int,toBase:int):
#     if 2>fromBase or frombase>16 or 2>toBase or toBase>16:
#         return "Wrong bases entered..."
#     dict = {
#         i:str(i) for i in range(0,10) 
#     }
#     dict[10] = "A"
#     dict[11] = "B"
#     dict[12] = "C"
#     dict[13] = "D"
#     dict[14] = "E"
#     dict[15] = "F"   
#     newDict = {}
#     for key in dict:
#         newDict[dict[key]] = key
    
#     res = 0
#     ##To Decimal
#     for i in num:
#         res=res*fromBase+newDict[i]
#     result = ""  
#     ##Conversion part
#     while res!=0:
#         result+=dict[res%toBase]
#         res = res//toBase
#     return result[::-1]

# print(convert("16",7,10))


### Exercise 106: Days in a Month
def dayCount(month,year):
    long = [1,3,5,7,8,10,12]
    if month<1 or month>12:
        return -1
    elif month==2:
        return 29 if year%4==0 else 28
    elif month in long:
        return 31
    else:
        return 30

# print(dayCount(20,2025))
### Exercise 107: Reduce a Fraction to Lowest Terms
# def reduceFraction(a,b):
#     divisor = min(a,b)
#     while a%divisor!=0 or b%divisor != 0:
#         divisor-=1
#     aR=int(a/divisor)
#     bR=int(b/divisor)
#     w = len(str(max(a,b)))*2
#     print(f"{center(str(a),w)}{' '*(w-1)}{center(str(aR),w)}\n" +  
#           f"{'-'* w} = {'-'* w}\n" + 
#           f"{center(str(b),w)}{' '*(w-1)}{center(str(bR),w)}\n")

# reduceFraction(62,63)

### Exercise 108: Reduce Measures
#    measures 
# 1 cup --> 16 tablespoons
# 1 tablespoon --> 3 teaspoons
# def reduceMeasures(count,unit:str):

#    if unit == "cup":
#        return f"{count} cups"
#    elif unit =="tablespoon":
#        cups = f"{count//16} cup" if count//16!=0 else ""
#        table = f"{count%16} tablespoon" if (count%16)!=0 else ""
#        return f"{cups+'s' if count//16>1 else cups} {table +'s' if (count%16)>1 else table }"
#    elif unit == "teaspoon":
#        cups = f"{count//48} cup" if count//48!=0 else ""
#        table = f"{(count%48)//3} tablespoon" if (count%48)//3!=0 else ""
#        tea =  f"{(count%48)%3} teaspoon" if (count%48)%3!=0 else ""
#        return f"{cups+'s' if count//48>1 else cups} {table +'s' if (count%48)//3>1 else table } {tea+'s' if (count%48)%3>1 else tea}"

# print(reduceMeasures(53,"tablespoon"))

### Exercise 109: Magic Dates
months = {
        'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9,
        'October' : 10,
        'November' : 11,
        'December' : 12
    }

monthsSwaped = {}
for i in months:
    monthsSwaped[months[i]] = i
print(months.values())
def isMagic(date):
    global months
    date = date.split(" ")
    if months[date[0]]*int(date[1])==int(date[2])%100:
        return True
    
    return False

def findAllMagics(start,end):
    global monthsSwaped
    q = 1
    for year in range(start,end+1):
        for month in monthsSwaped:
            for day in range(1,dayCount(month,year)+1):
                date = f"{monthsSwaped[month]} {day} {year}"
                if isMagic(date):                    
                    print(f"{q}) {date}")
                    q+=1
                    
                
findAllMagics(1801,2001)        