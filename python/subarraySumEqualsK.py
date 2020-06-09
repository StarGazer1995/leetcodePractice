class solution: #TODO caannot solve the case when nums have negative elements
    def subarraySumEqualsK(self,nums,k):
        dp = [0] * (k+1)
        dp[0] = 1
        count = 0
        for i in nums:
            for j in range(k,i-1,-1):
                dp[j] = dp[j] or dp[j-i]
                if(dp[k]==1):
                    count+=1
                    dp[k]=0
        return count

nums = [1,1,1]
k = 2

print(solution().subarraySumEqualsK(nums,k))