class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def backtrack(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0
            key = (i, current_sum)
            if key in memo:
                return memo[key]
            add = backtrack(i + 1, current_sum + nums[i])
            subtract = backtrack(i + 1, current_sum - nums[i])
            memo[key] = add + subtract
            return memo[key]

        return backtrack(0, 0)
nums = [1, 1, 1, 1, 1]
target = 3
sol = Solution()
print(sol.findTargetSumWays(nums, target))  # Output: 5        
