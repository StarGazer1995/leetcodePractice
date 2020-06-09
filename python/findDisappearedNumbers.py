class solution:
    def findDisappearedNumber(self,nums):
        n = len(nums)
        temp = [0] * n
        for i in nums:
            temp[i-1]+=1
        ans = []
        for i in range(n):
            if temp[i]==0:
                ans.append(i+1)
        return ans

nums=[4,3,2,7,8,2,3,1]
print(solution().findDisappearedNumber(nums))