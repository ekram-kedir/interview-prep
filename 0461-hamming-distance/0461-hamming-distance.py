class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        start = x ^ y
        value = 0
        
        while start > 0:
            value += start & 1
            start = start >> 1
            
        return value
        