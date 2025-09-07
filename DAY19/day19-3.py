class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        for num in nums2:
            if count.get(num, 0) > 0:
                result.append(num)
                count[num] -= 1

        return result
sol = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print("Intersection:", sol.intersect(nums1, nums2))