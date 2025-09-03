class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]  

        for char in s:
            if char == '(':
                stack.append(0)  
            else:
                last = stack.pop()
                if last == 0:
                    stack[-1] += 1  
                else:
                    stack[-1] += 2 * last  
        return stack[0]

sol = Solution()
s = "(()(()))"
output = sol.scoreOfParentheses(s)
print("Score of parentheses:", output)