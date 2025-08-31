class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1  
            else:
                right = mid  
        return left  
arr = [1, 3, 5, 7, 6, 4, 2]
sol = Solution()
print(sol.peakIndexInMountainArray(arr))  # Output: 3    