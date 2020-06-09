class solution:
    def subset(self,nums):
        list = [[]]
        nums.sort()
        self.backtrack(list,[],nums,0)
        return list
    def backtrack(self,list,temp,nums,start):
        tem = temp
        list.append(tem)
        for i in range(start,len(nums)):
            tem.append(nums[i])
            self.backtrack(list,tem,nums,i+1)
            tem.pop()

nums = [1,2,3]
print(solution().subset(nums))