class solution:
    def wordBreak(self,s,worddict):
        word = set()
        for i in worddict:
            word.add(i)
        res = [False] * (len(s)+1)
        res[0] = True

        for end in range(1,len(s)+1):
            for start in range(end):
                if(res[start] and s[start:end] in word):
                    res[end] = True
                    break
        return res[len(s)]

s = "aaaaaaa"
word = ["aaa","aaaa","sand","and","dog"]
print(solution().wordBreak(s,word))