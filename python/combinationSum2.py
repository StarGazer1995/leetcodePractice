class solution:
    def combinationSum2(self,candidates,target):
        ssum= sum(candidates)
        if(ssum<target):
            return 0
        tar = (ssum-target)//2
        n = len(candidates)
        dp = [[0]]*(tar+1)
        dp[0] = [[1]]
        for i in range(n):
            j = target
            while (j>=nums[i]):
                dp[j].append(j-nums[i])
                j-=1
        return dp[-1]

nums=[10,1,2,7,6,1,5]
target = 8

print(solution().combinationSum2(nums,target))