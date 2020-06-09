class solution:
    def longestParentheses(self,s):
        long = 0
        long_temp = 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if (s[i] == '('):
                long_temp += 1
            if (s[i] == ')' and long_temp > 0):
                dp[i] = 2 + dp[i - 1]
                if (i - dp[i] > 0):
                    dp[i] += dp[i - dp[i]]
                long_temp -= 1
            long = max(long, dp[i])

        return long

s = '()(()'
print(solution().longestParentheses(s))
