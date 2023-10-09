class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        
        def dfs(mask , op):
            
            if mask in memo:
                return memo[mask]
            
            for indx1 in range(len(nums)):
                for indx2 in range(indx1 + 1 , len(nums)):
                    
                    if (1 << indx1) & mask or (1 << indx2) & mask:
                        continue
                        
                    generateMask = mask | (1 << indx1) | (1 << indx2) 
                    result = op * gcd(nums[indx1] , nums[indx2])
                    memo[mask] = max(memo[mask] , result + dfs(generateMask , op + 1))
                    
            return memo[mask]
        return dfs(0 , 1)
                    