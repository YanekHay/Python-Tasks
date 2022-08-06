### Binary search
def find(num,arr,start,end):
    mid = (end+start)//2
    if arr[mid]==num:
        return mid
    elif arr[mid]>num:
        return find(num,arr,start,mid-1)
    elif arr[mid]<num:
        return find(num,arr,mid+1,end)
    

arr = [12,52,0,5,1,6544,21]
start = 0
end = len(arr)

num = int(input("Enter a number to search >>> "))
arr.sort()
print(arr)
print(find(num,arr,start,end))
