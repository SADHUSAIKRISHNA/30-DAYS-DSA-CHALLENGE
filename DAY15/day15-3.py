class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  
            else:
                stack.append(char)

        return ''.join(stack)

sol = Solution()
s = "abbaca"
output = sol.removeDuplicates(s)
print("Final result:", output)