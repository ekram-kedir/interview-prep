class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        constant = 1
        
        for bracket in range(len(s)):
            if s[bracket] == "(" and s[bracket + 1] == ")":
                score += constant
            if s[bracket] == "(":
                constant *= 2
            if s[bracket] == ")":
                constant = constant//2
        return score
                
                