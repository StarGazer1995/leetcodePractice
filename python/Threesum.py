class Solution:
    def helper(self,nums,temp,res,pos):
        if(len(temp)==3):
            if(sum(temp)==0):
                if temp not in res:
                    res.append(temp)
                    return
            temp.pop()
        if pos>len(nums)-1:
            return
        temp_ = temp.copy()
        temp_.append(nums[pos])
        self.helper(nums,temp_,res,pos+1)
    def Threesum(self,nums):
        nums.sort()
        res = []
        temp = []
        if len(nums)==0:
            return res
        for pos in range(len(nums)):
            temp = [nums[pos]]
            for i in range(pos+1,len(nums)):
                self.helper(nums,temp,res,i)
        return res

nums = [-2,-1,1,2]
print(Solution().Threesum(nums))