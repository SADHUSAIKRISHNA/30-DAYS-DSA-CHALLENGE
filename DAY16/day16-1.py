class Solution(object):
    def lemonadeChange(self, bills):
        five, ten = 0, 0  

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
bills = [5, 5, 10, 10, 20]
solution = Solution()
result = solution.lemonadeChange(bills)
print("Can give change to all customers?" , result)