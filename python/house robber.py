class solution:

    def house_robber(self,nums):
        ans_a = 0
        ans_b = 0
        for i in range(len(nums)):
            if (i % 2 == 0):
                ans_a = max(ans_a+nums[i],ans_b)
            else:
                ans_b = max(ans_a,ans_b+nums[i])
        print(max(ans_a,ans_b))

nums = [2,1,1,2]
solution().house_robber(nums)
