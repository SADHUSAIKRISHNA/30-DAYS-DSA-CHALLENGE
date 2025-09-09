class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()  
        result = []
        def backtrack(start, currentSubset):
            result.append(list(currentSubset))  
            for i in range(start, len(nums)):
                
                if i > start and nums[i] == nums[i - 1]:
                    continue

                currentSubset.append(nums[i])     
                backtrack(i + 1, currentSubset)   
                currentSubset.pop()               
        backtrack(0, [])
        return result
sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))    