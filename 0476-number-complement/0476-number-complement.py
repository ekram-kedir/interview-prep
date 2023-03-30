class Solution:
    def findComplement(self, num: int) -> int:
        
        start = 1
        while start <= num:
            start = start << 1
        return (start - 1) ^ num