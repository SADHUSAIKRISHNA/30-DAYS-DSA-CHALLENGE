class Solution(object):
    def getConcatenation(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        return nums + nums
sol = Solution()
print(sol.getConcatenation([1, 2, 3]))        