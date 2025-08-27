class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for num in nums1:
            found = False
            next_greater = -1
            index = nums2.index(num)
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    next_greater = nums2[i]
                    break

            result.append(next_greater)

        return result
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
    
sol = Solution()
output = sol.nextGreaterElement(nums1, nums2)
print("Next greater elements:", output)
    