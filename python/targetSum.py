class solution:
    def dfs(self,nums,current,target,signal):
        if len(nums)==0:
            if current == target:
                return 1
            else:
                return 0
        else:
            cur_temp = current
            if(signal=='-'):
                cur_temp -= nums[0]
            elif(signal=='+'):
                cur_temp += nums[0]
            slc = nums[1:]
            road1 = self.dfs(slc,cur_temp,target,'-')
            road2 = self.dfs(slc,cur_temp,target,'+')
            return road1+road2
    def targetSum(self,nums,target):
        ans1 = self.dfs(nums,0,target,'-')//2
        ans2 = self.dfs(nums,0,target,'+')//2
        return ans1+ans2

nums = [1,1,1,1,1]
target = 3
print(solution().targetSum(nums,target))