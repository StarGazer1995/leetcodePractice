
class Solution:
    def dfs(self, nums, step):
        max_dis = nums[0]
        if(max_dis ==0):
            return
        if (len(nums) == 1):
            self.step = step
            return
        for i in range(max_dis, 0, -1):
            if i >= len(nums):
                self.step = step + 1
                return
            else:
                self.dfs(nums[i:], step + 1)
            self.ans = min(self.step, self.ans)


    def jump(self,nums):
        self.step = int(len(nums))
        self.ans = int(len(nums))
        step = 0

        n = len(nums)
        nextStep = []
        maxArray = []
        for i in range(n):
            nextStep.append(i+nums[i])
            temp = 0
            if(i>0):
                temp = maxArray[i-1]
            maxArray.append(max(nextStep[i],temp))
        idx = 0
        count = 0
        while(idx<n-1):
            idx = maxArray[idx]
            count += 1

        return count
nums = [2,3,1,1,4]
print(Solution().jump(nums))
