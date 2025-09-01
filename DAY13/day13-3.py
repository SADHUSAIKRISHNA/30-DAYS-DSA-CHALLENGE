class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        key_map = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        index = key_map[ruleKey]
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count

# Example usage
items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"]
]

ruleKey = "type"
ruleValue = "phone"

sol = Solution()
print("Matching Count:", sol.countMatches(items, ruleKey, ruleValue))