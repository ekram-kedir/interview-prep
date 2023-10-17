class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod = 10**9 + 7
        half = int(n // 2)
        if n % 2 == 0:
            return ((pow(5,half, mod)) * (pow(4,half,mod))) % mod
        return (((pow(5,half,mod)) * (pow(4,half,mod))) * 5) % mod