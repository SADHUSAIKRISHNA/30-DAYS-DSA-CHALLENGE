class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []       
        current_sum = 0   
        for num in nums:
            current_sum += num       
            result.append(current_sum)  

        return result
sol = Solution()
print(sol.runningSum([1, 2, 3, 4])) 