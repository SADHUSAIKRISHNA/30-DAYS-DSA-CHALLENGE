class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1  
s = "sadhu sai"
solution = Solution()

print("Index of first unique character:", solution.firstUniqChar(s))
