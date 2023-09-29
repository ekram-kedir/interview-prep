class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        length = len(satisfaction)
        satisfaction.sort()
        @cache
        def helper(index , multiply):
            
            if index >= length:
                return 0
            
            pick = helper(index + 1, multiply + 1) + (satisfaction[index] * multiply) 
            dont_pick = helper(index + 1 , multiply)
            
            return max(pick , dont_pick)
        
        return helper(0 , 1)
            