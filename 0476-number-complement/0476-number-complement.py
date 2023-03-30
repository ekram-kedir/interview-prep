class Solution:
    def findComplement(self, num: int) -> int:
        
        power = floor(log(num , 2))
        value = 2 ** power
        return (2 * value) - num - 1