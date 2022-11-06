# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# ANSWER
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ans=0
        for i in tokens:
            if i=="+":
                prev=stack.pop()
                curr=stack.pop()
                ans=(int(prev)+int(curr))
                stack.append(ans)
            elif  i=="-":
                prev=stack.pop()
                curr=stack.pop()
                ans=(int(curr)-int(prev))
                stack.append(ans)
            elif  i=="/":
                prev=stack.pop()
                curr=stack.pop()
                ans=(int(int(curr)/int(prev)))
                stack.append(ans)
            elif i=="*":
                prev=stack.pop()
                curr=stack.pop()
                ans=(int(prev)*int(curr))
                stack.append(ans)
            else:
                stack.append(i)
        return int(stack[0])
