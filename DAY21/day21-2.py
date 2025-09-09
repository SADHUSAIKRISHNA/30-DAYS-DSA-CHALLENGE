class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  
        results = []

        def findCombos(index, currentCombo, currentSum):
            if currentSum == target:
                results.append(list(currentCombo))
                return
            if currentSum > target:
                return

            for i in range(index, len(candidates)):
               
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                currentCombo.append(candidates[i]) 
                findCombos(i + 1, currentCombo, currentSum + candidates[i])  
                currentCombo.pop() 

        findCombos(0, [], 0)
        return results
sol = Solution()
print(sol.combinationSum2([2, 5, 2, 1, 2], 5))        