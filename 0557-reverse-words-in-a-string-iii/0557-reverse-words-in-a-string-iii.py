class Solution:
    def reverseWords(self, s: str) -> str:
        
        answer = []
        words = s.split()
        
        for w in words:
            w = w[::-1]
            answer.append(w)
            
        return " ".join(answer)