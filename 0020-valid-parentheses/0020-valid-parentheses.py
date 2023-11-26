class Solution:
    def isValid(self, s: str) -> bool:
        
        opened_bracket = "({["
        closed_bracket = ")}]"
        
        stack = []
        
        for bracket in s:
            if bracket in opened_bracket:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    if closed_bracket.index(bracket) != opened_bracket.index(stack.pop()):
                        return False
                    
        return True if not stack else False
            