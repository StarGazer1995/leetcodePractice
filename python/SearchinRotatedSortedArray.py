class solution:
    def binarySearch(self,nums,start,end,target):
        while(start<=end):
            mid = start + (end-start)//2
            if(target<nums[mid]):
                end = mid-1
            elif(target==nums[mid]):
                return mid
            elif(target>nums[mid]):
                start = mid+1
        return -1
    def searchinRotadSortedArray(self,nums,target):
        if(not nums):
            return  None
        point = nums.index(max(nums))
        if(target>=nums[0]):
            ans = self.binarySearch(nums,0,point,target)
        else:
            ans = self.binarySearch(nums,point+1,len(nums)-1,target)
        return ans
nums = [4,5,6,7,8,0,1,2,3]
target = 5
print(solution().searchinRotadSortedArray(nums,target))

