### Leetcode 8. String to Integer

class Solution:
    def myAtoi(s: str) -> int:
        startInd = -1
        letters = "abcdefghijklmnopqrstuvwxyz."
        for i in range(len(s)):
            if s[i].isdigit():
                startInd = i
                break
        if startInd>=0:
            for i in range(0,startInd):
                if s[i] in letters:
                    return(0)
            number = ""
            if startInd>0 and (s[startInd-1]=="-" or  s[startInd-1]=="+")  :
                if startInd>1 and (s[startInd-2]=="-" or  s[startInd-2]=="+"):
                    return 0
                else:
                    number+=s[startInd-1]
            elif not("+" in s[:startInd] or "-" in s[:startInd]):
                number = ""
            else:
                return 0
            while startInd<len(s) and s[startInd].isdigit():
                
                number+=s[startInd]
                startInd+=1
            number = int(number)
            if number>2**31-1:
                return 2**31-1
            elif number<-(2**31):
                return -(2**31)
            else:
                return(number)
        else:
            return(0)
        

print(Solution.myAtoi(input("Enter a text >>> ")))
