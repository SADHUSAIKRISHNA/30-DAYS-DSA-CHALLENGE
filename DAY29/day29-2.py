class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]

            max_len = 1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(x, y))

            memo[i][j] = max_len
            return max_len

        return max(dfs(i, j) for i in range(m) for j in range(n))

# Example usage
sol = Solution()
matrix = [
  [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1]
]
print(sol.longestIncreasingPath(matrix))  # Output: 4