class Solution:
    def isHappy(self, n):
        seen = set()  

        while n != 1:
            if n in seen:
                return False  

           
            total = 0
            for digit in str(n):
                total += int(digit) ** 2
            n = total  

        return True 
num = 19
obj = Solution()
result = obj.isHappy(num)
print("Is", num, "a happy number?", result)    