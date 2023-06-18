class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        
        total = 0
        answer = 0
        
        for satisfy in satisfaction:
            
            total += satisfy
            if total < 0:
                break
            answer += total
            
        return answer