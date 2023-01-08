class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        p = 0
        p2 = 0
        
        for i in num1:
            p = 10 * p + int(i)
            
        for j in num2:
            p2 = 10 * p2 + int(j)
            
        return str(p * p2)