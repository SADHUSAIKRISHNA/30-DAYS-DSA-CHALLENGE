class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            curr = mid * (mid + 1) // 2  

            print("Trying mid = {}: needs {} coins".format(mid, curr))

            if curr == n:
                print("Exact match at row {}".format(mid))
                return mid
            elif curr < n:
                left = mid + 1
            else:
                right = mid - 1

        print("Maximum full rows = {}".format(right))
        return right


n = 8
sol = Solution()
result = sol.arrangeCoins(n)
print("\nWith {} coins, you can build {} full rows.".format(n, result))