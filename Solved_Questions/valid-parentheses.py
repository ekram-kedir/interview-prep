# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
########################_Solution_for_valid-parentheses_########################################3
class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket='({['
        close_bracket=')}]'
        stack=[]
        for i in s:
            if i in open_bracket:
                stack.append(i)
            elif i in close_bracket:
                if len(stack)==0:
                    return False
                elif close_bracket.index(i)!=open_bracket.index(stack.pop()):
                    return False
        if len(stack)==0:
            return True
        else:
            return False
