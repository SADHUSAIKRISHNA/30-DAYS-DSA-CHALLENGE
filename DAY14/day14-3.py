class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(max_sum):
            count, curr_sum = 1, 0
            for num in nums:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = 0
                curr_sum += num
            return count <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left
nums = [7,2,5,10,8]
k = 2
sol = Solution()
print(sol.splitArray(nums, k))     
    