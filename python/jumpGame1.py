class solution:
    def jumpGame1(self,nums):
       farestpos = 0
       for i in range(len(nums)-1):
           farestpos = max(farestpos, nums[i]+i)

       if (farestpos>=len(nums)):
           return True
       else:
           return False

nums = [1,0,3,0,1]
print(solution().jumpGame1(nums))