class solution:
    def dicbuild(self,p):
        dic_p = [0] * 26
        for i in p:
            dic_p[ord(i)-ord('a')]+=1
        return dic_p
    def findall(self,s,p):
        dic_p = self.dicbuild(p)
        ans = []
        for i in range(0,len(s)-len(p)+1):
            dic_s = self.dicbuild(s[i:i+len(p)])
            if(dic_p==dic_s):
                ans.append(i)
        return ans

s="ababababab"
p="aab"
print(solution().findall(s,p))