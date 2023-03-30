class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        value = bin(x ^ y)
        return str(value).count("1")
        