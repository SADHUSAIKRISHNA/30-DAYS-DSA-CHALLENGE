class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num  # XOR operation
        return result
sol = Solution()
numbers = [2, 3, 5, 3, 2]
print("The single number is:", sol.singleNumber(numbers))