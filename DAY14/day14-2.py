class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(capacity):
            curr_weight = 0
            required_days = 1
            for weight in weights:
                if curr_weight + weight > capacity:
                    required_days += 1
                    curr_weight = 0
                curr_weight += weight
            return required_days <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
sol = Solution()
print(sol.shipWithinDays(weights, days))  