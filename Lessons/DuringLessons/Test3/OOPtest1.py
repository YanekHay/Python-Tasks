'''
                    | TASK N1 |
Ունենք n ամբողջ թիվը, գտնել համապատասխանաբար n֊ի քանակով 
բոլոր բացվող և փակվող փակագծերի կոմբինացիաները


օրինակ
Մուտք՝ n = 3
Ելք՝ ["((()))","(()())","(())()","()(())","()()()»]
'''
# Գրեք Ձեր կոդը
# n = int(input("Enter a number >>> "))
# def buildPranths(n,permutation,res,isStart = True):
#    if n==0:
#       res.append(permutation)
#    else:
#       if permutation.count("(")<(n+len(permutation))//2:
#          buildPranths(n-1,permutation + "(",res,False)
#       if permutation.count("(")>permutation.count(")"):
#          buildPranths(n-1,permutation + ")",res,False)
#    if isStart:
#       return res

# print(buildPranths(2*n,"",[]))

'''
                    | TASK N2 |
Դուք բարձրանում եք սանդուղք: n Գագաթին հասնելու համար անհրաժեշտ են քայլեր :
Ամեն անգամ դուք կարող եք կամ բարձրանալ 1 կամ 2 աստիճաններ: 
Քանի՞ տարբեր եղանակներով կարող եք բարձրանալ գագաթ:


օրինակ 1
Մուտք. n = 2
Արդյունք. 2
Բացատրություն. Վերև բարձրանալու երկու եղանակ կա: 
1. 1 քայլ + 1 քայլ 
2. 2 քայլ
օրինակ 2
Մուտք. n = 3
Արդյունք. 3
Բացատրություն. Վերև բարձրանալու երեք եղանակ կա: 
1. 1 քայլ + 1 քայլ + 1 քայլ 
2. 1 քայլ + 2 քայլ 
3. 2 քայլ + 1 քայլ
'''
# Գրեք Ձեր կոդը
# def getVariants(n,variant,variants,isStart=True):   
#    if n==0:
#       variants.append(variant)
#    else:
#       variant.append(1)
#       getVariants(n-1,variant[:],variants,False)
#       if n-2>=0:
#          del variant[-1]
#          variant.append(2)
#          getVariants(n-2,variant[:],variants,False)
#    if isStart:
#       return variants

# n = int(input("Enter a number >>> "))

# res = getVariants(n,[],[])
# print(f"\nThere are {len(res)} possible ways\n{res}")

'''
                    | TASK N3 |
Հաշվի առնելով ամբողջ numթիվը, մի քանի անգամ ավելացրեք 
նրա բոլոր թվանշանները, մինչև արդյունքը ունենա միայն մեկ
թվանշան և վերադարձրեք այն:


օրինակ 1
Մուտք. num = 38
Արդյունք. 2
Բացատրություն. Գործընթացը 
38 --> 3 + 8 --> 11 
11 --> 1 + 1 --> 2 
Քանի որ 2-ն ունի միայն մեկ թվանշան, վերադարձրեք այն:

օրինակ 2
Մուտք՝ num = 0
Ելք՝ 0

'''
# Գրեք Ձեր կոդը
# def getOne(n):
#    while True:
#       num = 0
#       for digit in str(n):
#          num+=int(digit)
#       if num<10:
#          return num
#       n = num
      
# print(getOne(input("Enter a number >>> ")))

'''
                    | TASK N4 |
Դուք ունեք 10 րոպե ժամանակ ուսումնասիրելու համար, թե ինչ է երկուական ծառը
(bineary tree) և Հաշվի առնելով root երկուական ծառը, վերադարձրեք նրա հանգույցների 
արժեքների անհամակարգ անցումը :
 

օրինակ 1
( 1 )
   \
    \
     \
      \
     ( 2 )
      /
     /
    /
   /
( 3 )    
Մուտք՝ արմատ = [1,None,2,None,None,3]
Ելք՝ [1,3,2]

օրինակ 2
Մուտք՝ արմատ = []
Ելք՝ []

օրինակ 3
Մուտք՝ արմատ = [1]
Ելք՝ [1]
'''
# Գրեք Ձեր կոդը
# import binarytree as bt
# root = [1,None,2,None,None,3]
# tree = bt.build(root)
# def getNodes(root:bt,res,isStart = True):
#    if root:
#       getNodes(root.left,res,False)
#       res.append(root.val)
#       getNodes(root.right,res,False)
#       if isStart:
#          return res

# print(getNodes(tree,[]))
'''
                    | TASK N5 |
Տրվելով տողերի զանգված strs, խմբավորեք անագրամները միասին: 
Պատասխանը կարող եք վերադարձնել ցանկացած հերթականությամբ :

Անագրամը բառ կամ արտահայտություն է, որը ձևավորվում է 
մեկ այլ բառի կամ արտահայտության տառերը վերադասավորելու 
միջոցով՝ սովորաբար օգտագործելով բոլոր բնօրինակ տառերը 
ուղիղ մեկ անգամ:

օրինակ 
Մուտք՝: strs = ["eat","tea","tan","ate","nat","bat"]
Ելք՝: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''
# print(''.join(sorted("text",key = str.lower)))

# Գրեք Ձեր կոդը
# def arrange(strings:list[str]):
#    boxes = {}
#    for word in strings:
#       sortedword = ''.join(sorted(word.lower()))
#       try:
#          boxes[sortedword].append(word)
#       except:
#          boxes[sortedword]=[word]
   
#    return boxes.values()


# strs = ["eat","tea","tan","ate","nat","bat"]
# print(arrange(strs))