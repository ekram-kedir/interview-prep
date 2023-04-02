class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        
        return self.gcd(nums[-1] , nums[0])
    
    def gcd(self,a , b):
        if b == 0 :
            return a
        
        return self.gcd(b , a % b)