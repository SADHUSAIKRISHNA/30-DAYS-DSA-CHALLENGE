class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for num in nums1:
            found = False
            next_greater = -1

            # Find the index of num in nums2
            index = nums2.index(num)

            # Check elements to the right of index
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    next_greater = nums2[i]
                    break

            result.append(next_greater)

        return result