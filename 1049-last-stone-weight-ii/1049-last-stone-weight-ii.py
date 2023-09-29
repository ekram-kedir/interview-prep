class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        length = len(stones)
        memo = {}
        
        def helper(index , currentSum):
            
            if index >= length:
                return currentSum if currentSum >= 0 else inf
            
            if (index , currentSum) in memo:
                return memo[(index , currentSum)]
            
            positive = helper(index + 1, currentSum + stones[index])
            negative = helper(index + 1 , currentSum - stones[index])
           
            memo[(index , currentSum)] = min(positive , negative)
            return memo[(index , currentSum)]
            
        return helper(0 , 0)
        
            
            