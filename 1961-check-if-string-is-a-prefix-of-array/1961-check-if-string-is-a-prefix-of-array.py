class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        answer = ""
       
        for w in words:
            answer += w
            if answer == s:
                return True
        return answer == s