class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        answer = []
        
        for idx in range(len(num)-2):
            if len(set(num[idx:idx + 3])) == 1:
                answer.append(num[idx])
        return max(answer)*3 if len(answer) >= 1 else ""
            
        