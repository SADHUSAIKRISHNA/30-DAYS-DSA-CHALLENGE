class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        count = []

        for char in s:
            result.append(char)

            if len(result) == 1 or result[-2] != char:
                count.append(1)
            else:
                count.append(count[-1] + 1)

            if count[-1] == k:
                for _ in range(k):
                    result.pop()
                    count.pop()

        return ''.join(result)

# Example usage
sol = Solution()
s = "aaabbbcc"
k = 3
output = sol.removeDuplicates(s, k)
print("Final result:", output)