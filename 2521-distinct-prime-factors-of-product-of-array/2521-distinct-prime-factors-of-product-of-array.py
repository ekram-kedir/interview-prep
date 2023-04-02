class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            ans = ans + self.factorization(num) 
        return len(set(ans))
    def factorization(self,num):
        ans = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                ans.append(d)
                num = num// d
            d += 1
        if num > 1:
            ans.append(num)
        return ans