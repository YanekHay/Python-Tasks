class numbers:
    def __init__(self,numList:list[int]) -> None:
        self.numList = numList
    #### The overloading of __str__ method is just for studying purposes
    def __str__(self) -> str:
        if len(self.numList)<2:
            return str(0)
        else:
            max = 0
            for i in range(1,len(self.numList)):
                if abs(self.numList[i]-self.numList[i-1])>max:
                    max = abs(self.numList[i]-self.numList[i-1])
            return str(max)
    
    
test = numbers([2,4,1,0])
print(test)