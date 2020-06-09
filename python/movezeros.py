class solution:
    def movezeros(self,nums):
        mark = []
        for i in range(len(nums)):
            if(nums[i]==0):
                mark.append(i)
                nums.append(0)
        while(len(mark)>0):
            nums.pop(mark[-1])
            mark.pop()


nums = [0,0,1]
solution().movezeros(nums)
print(nums)
