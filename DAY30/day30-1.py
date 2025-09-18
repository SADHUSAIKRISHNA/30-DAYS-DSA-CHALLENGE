class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = 1  
        for i in range(1, rows):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for j in range(1, cols):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[rows-1][cols-1]
obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

sol = Solution()
print("Number of unique paths:", sol.uniquePathsWithObstacles(obstacleGrid))    