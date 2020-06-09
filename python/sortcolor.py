class Solution:
    def sortcolor(self,nums):
        count = [0,0,0]
        for i in nums:
            if(i ==0):
                count[0]+=1
            elif( i ==1):
                count[1]+=1
            else:
                count[2]+=1
        nums[0:count[]]
