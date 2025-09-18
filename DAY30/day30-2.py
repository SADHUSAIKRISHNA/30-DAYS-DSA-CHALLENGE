class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

sol = Solution()
print("Minimum path sum:", sol.minimumTotal(triangle))    