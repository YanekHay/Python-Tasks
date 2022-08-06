import math
########  COVID - 19
# class covid_19:
#     def __init__(self,temp) -> None:
#         self.temp = temp
    
#     def test(self):
#         if math.ceil(self.temp*math.pi)>=120 and math.ceil(self.temp*math.pi)<=128:
#             print("You Have coronavirus")
#         else:
#             print("Everything is ok")
            
# person = covid_19(float(input("Enter your body temperature >>> ")))
# person.test()

########  Find your name number
# print((ord("b")-97)%9,(ord("k")-97)%9,(ord("t")-97)%9)
# class nameNumber:
    
#     def __init__(self,name) -> None:        
#         self.name = name
        
#     def getnameNumber(self):
#         res = 0
#         for letter in self.name.lower():
#             res+=(ord(letter)-97)%9+1
#         return res
#     def isNameCommon(self):
#         if math.sqrt(self.getnameNumber())<5:
#             return "Yes"
#         else:
#             return "No"
# person = nameNumber("Shakira")
# print(person.isNameCommon())

########  Harry Potter
import random
possibleSpells = ["Avada Kedavra", "Crucio", "Imperio"]

class Harry:
    def __init__(self,spells:list[str]) -> None:
        self.spells = spells
    
    def fight(self):
        global possibleSpells
        Valdemort = [possibleSpells[random.randint(0,len(possibleSpells))] for i in range(0,len(possibleSpells))]
        self.points = 0
        for i in range(len(self.spells)):
            if self.spells[i]==Valdemort[i]:
                self.points+=1
        if self.points >=2:
            return f"You Won\nYour score is {self.points}"
        else:
            return f"You Lost\nYour score is {self.points}"

spells = []
for i in range(0,3):
    while True:
        inp = input("Avada Kedavra, Crucio, Imperio ...\n>>> ")
        if inp in possibleSpells:
            spells.append(inp)
            break
        else:
            print("Wrong input!!!")
        
player = Harry(spells)
print(player.fight())