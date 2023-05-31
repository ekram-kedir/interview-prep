class Solution:
    def fib(self, n: int) -> int:
        
        result = [ i for i in range(n)] 
        
        if n <= 1:
            return n
        
        else:
            
            result[0] = 1
            result[1] = 1

            for i in range(2,n):

                result[i] = result[i - 1] + result[i - 2]

            return result[-1]
