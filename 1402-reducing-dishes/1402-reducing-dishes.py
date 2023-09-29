class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        max_satisfaction = 0
        length = len(satisfaction)
        
        satisfaction.sort()
        
        for ind in range(length):
            sati = 0
            for indx in range(ind , length):
                sati += (indx + 1 - ind) * satisfaction[indx]
            max_satisfaction = max(max_satisfaction , sati)
            
        return max_satisfaction