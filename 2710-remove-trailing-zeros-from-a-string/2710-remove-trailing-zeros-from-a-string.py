class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        right = len(num) - 1
        
        while right >= 0:
            if num[right] == "0":
                right -= 1
            else:
                return num[:right + 1]
            