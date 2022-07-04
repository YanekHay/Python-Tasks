# LeetCode 33. Search in Rotated Sorted Array
nums = [4,5,6,7,0,1,2,8]
target = 0
correct = []

if target in nums:
    correct = nums[nums.index(target):]
    print(nums[nums.index(target):])
    correct.extend(nums[:nums.index(target)])
    sorted = correct[:]
    sorted.sort()
    print(sorted)
    if sorted==correct:
        print(nums.index(target))
    else:
        print(-1)
else:
    print(-1)
    