class Solution(object):
    def validPalindrome(self, s):
        def is_pal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return is_pal(s, i+1, j) or is_pal(s, i, j-1)
            i += 1
            j -= 1
        return True
# Example usage
sol = Solution()
s = "abca"
print("Input:", s)
print("Can become palindrome by removing at most one character?", sol.validPalindrome(s))