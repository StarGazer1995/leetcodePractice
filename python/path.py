class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp =[]
        for i in range(row):
            dp.append([])
            for j in range(col):
                if (i==0 or j == 0):
                    dp[i].append(1)
                else:
                    dp[i].append(0)
        for i in range(1, row):
            for j in range(1, col):
                if(not obstacleGrid[i][j]):
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[row-1][col-1]


input = [[0,0,0],[0,1,0],[0,0,0]]

print(Solution().uniquePathsWithObstacles(input))