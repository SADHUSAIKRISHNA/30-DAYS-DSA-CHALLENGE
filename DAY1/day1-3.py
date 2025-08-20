class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        last_pos = 0

        
        for num in nums:
            if num != 0:
                nums[last_pos] = num
                last_pos += 1

        
        while last_pos < len(nums):
            nums[last_pos] = 0
            last_pos += 1
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)            