class solution:
    def maxProduct(self,nums):
        ans = max(nums)
        imax = nums[0]
        imin = imax
        for i in range(len(nums)):
            if (nums[i]<0):
                imax,imin = imin,imax
            imax = max(imax,imax*nums[i])
            imin = min(imin,imin*nums[i])

        ans = max(ans,imax)
        return ans


nums = [-2,-1]
print(solution().maxProduct(nums))