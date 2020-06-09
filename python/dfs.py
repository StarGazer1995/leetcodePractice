import math
class Solution:
    def ans(self,n,deepth):
        self.C = 1
        self.sqaue = 0
        self.ans = 0
        def dfs(n,deepth):
            if deepth == 1:
                for i in range (1, n+1):
                    if n % i != 0:
                        continue
                    else:
                        self.C = i
                        dfs(n//i, deepth+1)
            if deepth == 2:
                for i in range (1, n+1):
                    if n % i != 0:
                        continue
                    else:
                        R = i
                        L = n//i
                    self.ans = max(self.sqaue, (self.C+1)*(R+2)*(L+2))
        dfs(n, deepth)
        return self.ans-n
    def sqnumber(self,num):
        stack = [(n,0)]
        visited = [0] * (n+1)
        visited[n] = 1
        while stack:
            num,step = stack.pop(0)
            i = 1
            tmp = num - i**2
            while tmp >= 0:
                if tmp == 0:
                    return step + 1
                if not visited[tmp] == 1:
                    visited[tmp] = 1
                    stack.append((tmp, step+1))
                i += 1
                tmp = num - i**2

    def coinChange(self, coins, amount):
        Max = float('inf')
        dp = [0] + Max * amount
        for i in range(1, amount+1):
            dp[i] = min(dp[i-c] if i>=c else Max for c in coins) + 1

        return [dp[amount], -1][dp[amount] == Max]

    def jumpstairs(self, num):
        max = [0]
        dp = [0,1,2] + max * (num - 2)
        for i in range(3,num+1):
            dp[i] = dp[i-2]+dp[i-1]
        return dp[num]

print (Solution().jumpstairs(9))