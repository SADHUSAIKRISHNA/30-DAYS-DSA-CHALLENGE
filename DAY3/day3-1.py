class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
num = int(input("Enter a number: "))
solution = Solution()
if solution.isPalindrome(num):
    print("Yes, it's a palindrome!")
else:
    print("Nope, not a palindrome.")