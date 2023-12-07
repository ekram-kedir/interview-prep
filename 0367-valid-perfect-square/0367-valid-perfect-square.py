class Solution:
    def isPerfectSquare(self, num: int) -> bool:
            left, right = 0, num + 1
            while left < right:
                mid = left + (right - left) // 2
                if mid * mid > num:
                    right = mid
                elif mid * mid < num:
                    left = mid + 1
                else:
                    return True
            return False