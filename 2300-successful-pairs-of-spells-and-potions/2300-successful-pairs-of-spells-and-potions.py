class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        answer = [0] * len(spells)
        
        for i in range(len(spells)):
            
            left = -1
            right = len(potions)
            while left + 1 < right:
                mid = left + (right - left)//2
                if spells[i] * potions[mid] >= success:
                    right = mid
                else:
                    left = mid
            
            answer[i] =len(potions) - right
        
        return answer
       