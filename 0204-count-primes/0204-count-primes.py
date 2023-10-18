class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n)]
        
        if n == 0 or n == 1:
            return 0
        
        start = 2
        while (start * start) <= n:
            if prime[start] == True:
                for index in range(start * start , n , start):
                    prime[index] = False
            start += 1
        count_primes = Counter(prime)[True]
        
        return count_primes - 2