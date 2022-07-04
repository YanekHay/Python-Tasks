# մուտք կամայական թիվ, եթե ստացվումա եռանկյուն՝՝ 15, 21, 
# 0 
# 1 0
# 2 6 00
# 3 7 10 00
# 4 8 11 13 00
# 5 9 12 14 15 00

# Correct numbers are 1, 3, 6, 10, 15, 21, 28, 36, ...

n = int(input("Enter a number >>> "))
correctNum = 1
step=1
while(abs(correctNum-n)>step):
    correctNum+=step+1
    step+=1

print(f"Num: {correctNum}\nStep: {step}")
output = ""
for i in range(1,step+1):
    output =f"{output}{i:<3}"   
    val = i+step-1
    for j in range(i-1):
        output= f"{output} {val:<3}"
        val+=step-j-2
    output=f"{output}\n"

print(output)