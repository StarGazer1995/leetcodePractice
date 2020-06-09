class solution:
    def backtrack(self,list,temp,nums):
        if(len(temp)==len(nums)):
            list.append(temp)
        else:
            for i in range(len(nums)):
                if(nums[i] in temp):
                    continue
                temp.append(nums[i])
                self.backtrack(list,temp,nums)
                temp.pop()
    def permutations(self,nums):
        list = [[]]
        nums.sort()
        temp = []
        self.backtrack(list,nums,temp)
        return list

nums=[1,2,3]
print(solution().permutations(nums))