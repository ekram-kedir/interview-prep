class Solution:
    def totalMoney(self, n: int) -> int:
        
        start = 1
        end = 7
        ans = 0
        
        while n >= 7:
            n -= 7
            ans += (7/2) * ((2 * start) + (6))
            start += 1
            end += 1
            
        while n > 0:
            ans += start
            start += 1
            n -= 1
        return int(ans)