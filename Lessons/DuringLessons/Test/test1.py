# | -.-.-.-.-.-  Test - 1 -.-.-.-.-.- |
# ---------------------------------------------------------------
'''1. Write a function to find the longest common prefix 
string amongst an array of strings.If there is no common 
prefix, return an empty string "".'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
'''Example - 2'''
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
'''Example - 3'''
# Input: strs = ["reflower","flow","flight"]
# Output: ""
# ---------------------------------------------------------------
# Your code :)
# ["flow","flower","flight"]


strs = ["dog","racecar","car"]

strs.sort(key=len)
pref = strs[0].lower()

for i in range(0,len(strs)+1): 
    b=True
    for j in range(1,len(strs)):         
        if pref != strs[j][:len(pref)].lower():
            # print(strs[j][:len(pref)].lower(),pref)
            b=False
            break
    if b==False:
        pref = pref[:len(pref)-1] if len(pref)>1 else ""
        
print(f'\t1.\n\t\t{"---" if pref=="" else pref}\n')    

# ---------------------------------------------------------------
'''2. Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
'''Example - 2'''
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''Example - 2'''
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# ---------------------------------------------------------------
# Your code :)
# x= int(input("Enter an integer >>> "))
x = 121
def isPalindrome(x:str)->bool:
  return x==x[::-1]

# def isPalindrome(x:int)->bool:
#   if x<0:
#     return False
#   xcopy = x
#   revnum = 0
#   while x!=0:
#     revnum = revnum*10+x%10
#     x = x//10

#   if revnum==xcopy:
#     return True
#   else:
#     return False

print(f'\t2.\n\t\t{isPalindrome(str(x) if not isinstance(x,str) else x)}\n')
# ---------------------------------------------------------------
'''3. Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
'''Example - 2'''
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
'''Example - 3'''
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
# ---------------------------------------------------------------
# Your code :)
# text = input("Enter a text >>> ")
text  = "luffy is still joyboy"
text = text.strip()
lastword = ""
for i in range(len(text)-1,-1,-1):
  if text[i]==" ":
    break
  lastword+=text[i]
print(f'\t3.\n\t\t{len(lastword)}\n')
# ---------------------------------------------------------------
'''4. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: s = "()"
# Output: true
# ---------------------------------------------------------------
'''Example - 2'''
# Input: s = "()[]{}"
# Output: true
# ---------------------------------------------------------------
'''Example - 3'''
# Input: s = "(]"
# Output: false
# ---------------------------------------------------------------
# Your code :)
s = "[][{({}{})}][]"
openers = "{[("
closers = "}])"
def isCorrect(text:str)->bool:
  global openers,closers
  checker = True
  for i in range(0,3):
    if text.count(openers[i]) == text.count(closers[i]):
      opind=[]
      clind=[]
      for j in range(len(text)):
        if text[j] == openers[i]:
          opind.append(j)
        elif text[j] == closers[i]:
          clind.append(j)
          
      for j in range(len(opind)):
        if clind[j]<opind[j]:
          return False
    else:
      return False

  return True

print(f'\t4\n\t\t{isCorrect(s)}\n')
# ---------------------------------------------------------------
'''5. You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# ---------------------------------------------------------------
'''Example - 2'''
# Input: list1 = [], list2 = []
# Output: []
# ---------------------------------------------------------------
'''Example - 3'''
# Input: list1 = [], list2 = [0]
# Output: [0]
# ---------------------------------------------------------------
# Your code :)
list1 = [1,2,4]
list2 = [5,3]
merged = []
for i in range(max(len(list1),len(list2))):
  try:
    list1[i]
  except:
    None
  else:
    merged.append(list1[i])
  try:
    list2[i]
  except:
    None
  else:
    merged.append(list2[i])
    
print(f'\t5.\n\t\t{merged}')
# ---------------------------------------------------------------

'''
                   ______
                  |      |
             \____|______|____/
                | (_)  (_) |
                |    ||    |
                | \______/ |
                |__________|      / / / 
               _____|  |_____    |_  _|
             / |            |\    / /
            / /|            | \  / /
           / / |            |\ \/ /
          | \  |            | \__/ 
           \ \ |            |  
            \ \|            |
             \ |____________|
               |            |
               |    ____    |
               |   /    \   |
               |   |    |   |
               |   |    |   |
               |   |    |   |
               |   |    |   |
               |___|    |___|               




'''          
