### Print all possible permulations of this list
myList = [1,2,5,6,5]
arr = myList[:]
arr.sort()

depth = len(arr)
q = 0

def loop(level,res,arr):
    global depth,q
    if level == depth:
        q+=1
        print(res)
        return
    else:
        for i in range(len(arr)):
            cpy = arr[:]
            cpy.remove(arr[i])
            res.append(str(arr[i]))
            loop(level+1,res,cpy) 
            
            del res[-1]
            

loop(0,[],arr)
print(f"\n\nThere are {q} permulations of {myList}")