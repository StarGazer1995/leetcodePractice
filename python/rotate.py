class solution:
    def rotate(self, nums)->None:
        nums.reverse()
        for i in range(len(nums[0])):
            for j in range(i,len(nums[0])):
                nums[j][i],nums[i][j] = nums[i][j],nums[j][i]
        return nums
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(nums)
print(solution().rotate(nums))