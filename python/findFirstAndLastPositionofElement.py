class Solution:
    def searchRange(self,nums,target,start,end):
        def search(nums,target):
            l = 0; r = len(nums) - 1
            while(l<=r):
                mid = (r - l)//2 + l
                if nums[mid]<target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l


        if(len(nums)==0):
            return [-1, -1]
        idx_1 = search(nums, target)
        idx_2 = search(nums, target+1) - 1
        if(idx_1 < len(nums) and nums[idx_1] == target):
            return [idx_1, idx_2]
        else:
            return [-1, -1]


