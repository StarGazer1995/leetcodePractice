class solution:
    def findtheDuplicateNumber(self,nums):
        nums.sort()
        for i in range(len(nums)):
            if (i != nums[i]-1):
                return nums[i]
nums = [1,3,4,2,2]
print(solution().findtheDuplicateNumber(nums))