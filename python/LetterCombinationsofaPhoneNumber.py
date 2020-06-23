class Solution:
    def __init__(self):
        self.dic = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

    def combination(self,lis, stri):
        if lis:
            leng = len(lis)
            while(leng>0):
                tmp = lis[0]
                lis.pop(0)
                for i in self.dic[stri]:
                    lis.append(tmp+i)
                leng -= 1
        else:
            for j in self.dic[stri]:
                lis.append(j)
        return lis

    def letterCombinations(self, digits):
        lis=[]
        for i in digits:
            lis = self.combination(lis, i)
        return lis

s = '23'
lis = Solution().letterCombinations(s)
for i in lis:
    print(i)