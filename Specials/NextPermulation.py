##LeetCode 31. Next Permutation
class Solution:
    def nextPermutation(nums)->None:
        pointer=0
        length=len(nums)
        if length<=2:
            return nums.reverse()
        pointer=length-2
        while(pointer>=0 and nums[pointer]>=nums[pointer+1]):
            pointer-=1
        if pointer==-1:
            return nums.reverse()
        for i in range(length-1,pointer,-1):
            if nums[pointer]<nums[i]:
                nums[pointer],nums[i]=nums[i],nums[pointer]
                break

        nums[pointer+1:]=reversed( nums[pointer+1:])
        print(nums)

Solution.nextPermutation([2,9,3,5,2])