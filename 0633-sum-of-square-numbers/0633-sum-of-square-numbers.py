class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        
        start = 0
        for i in range(c + 1):
            if i ** 2 <= c:
                start = i
            else:
                break
        right = start
        
        while left <= right :
            if (left) ** 2 + (right) ** 2 < c:
                left += 1
            elif (left) ** 2 + (right) ** 2 > c:
                right -= 1
            else:
                return True
        return False