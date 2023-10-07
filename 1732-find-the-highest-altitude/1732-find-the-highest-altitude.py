class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        answer = [0 for _ in range(len(gain) + 1)]
        
        for ind in range(1, len(gain) + 1):
            answer[ind] = answer[ind - 1] + gain[ind - 1]
        return max(answer)