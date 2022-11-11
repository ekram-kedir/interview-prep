class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = []
        stack = []
        res= " "
        for i in s:
            stack.append(i)
            if i == ")":
                stack.pop()
                while stack[-1] != "(":
                    ans.append(stack.pop())
                stack.pop()
                stack += ans
                ans=[]
        return "".join(stack)