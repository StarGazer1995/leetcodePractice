class solution:
    def dfs(self,nums,current,target):
        ans = False
        if not nums:
            return False
        temp = current + nums[0]
        if temp == target:
            return True
        if temp > target:
            return False
        for i in range(1,len(nums)):
            sli = nums[i:]
            ans = ans or self.dfs(sli,temp,target)
        return ans
    def canPartition(self,nums):
        target = sum(nums)
        if target%2!=0:
            return False
        target = target/2
        nums.sort()
        while(target!=0 and target>0):
            if(target-nums[-1] not in nums):
                target



nums = [1,5,11,5]
print(solution().canPartition(nums))