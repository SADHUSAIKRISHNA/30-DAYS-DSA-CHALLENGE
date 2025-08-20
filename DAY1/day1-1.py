class Solution(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        return self.num1 + self.num2
result = Solution(10, 20)
print("result:", result.sum())