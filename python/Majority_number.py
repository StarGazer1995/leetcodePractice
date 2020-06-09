class solution:
    def Marjority_number(self,nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        dic = {}
        for i in nums:
            if( i not in dic.keys()):
                dic[i] = 0
            else:
                dic[i] += 1
                if(dic[i]>=length//2):
                    return i


nums = [3,2,3]
print(solution().Marjority_number(nums))