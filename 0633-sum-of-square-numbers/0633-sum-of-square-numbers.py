class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = (int)(math.sqrt(c)) 
        while left <= right :
            if (left) ** 2 + (right) ** 2 < c:
                left += 1
            elif (left) ** 2 + (right) ** 2 > c:
                right -= 1
            else:
                return True
        return False
