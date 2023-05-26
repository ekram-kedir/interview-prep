class Solution:
    def tribonacci(self, n: int , store = defaultdict(int)) -> int:
        
        if n == 0:
            return n
        elif n == 1 or n == 2:
            return 1
        elif n in store:
            return store[n]
        else:
            store[n] = self.tribonacci(n - 1,store) + self.tribonacci(n - 2,store) + self.tribonacci(n - 3,store)
            return store[n]
        