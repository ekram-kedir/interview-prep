class Solution:
    def countDigits(self, num: int) -> int:
                
        count = 0
        for divisor in str(num):
            if num % int(divisor) == 0:
                count += 1
        return count