class Solution:
    def minSteps(self, n: int) -> int:
        
        ans = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                ans += i
                n //= i
        if n > 1:
            ans += n
        return ans

        
                