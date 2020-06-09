class solution:
    def topkFrequent(self,nums,k):
        dic = {}
        for i in range(len(nums)):
            if (dic[i]==None):
                dic[i] = 1
            else:
                dic[i] += 1
        dic.fromkeys()
        key = dic.keys()
        key.sort()
        


nums =[-1,-1]
k = 1
print(solution().topkFrequent(nums,k))