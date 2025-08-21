class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

nums = [1, 2, 3, 4, 5, 6, 2]  
solution = Solution()
print("Contains duplicate:", solution.containsDuplicate(nums))