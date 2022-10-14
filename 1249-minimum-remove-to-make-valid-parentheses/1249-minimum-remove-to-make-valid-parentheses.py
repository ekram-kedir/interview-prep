class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        lis=list(s)
        for idx,char in enumerate(lis):
            if char=="(":
                stack.append(idx)
            elif char==")":
                if stack:
                    stack.pop()
                else:
                    lis[idx]=""
        while stack:
            lis[stack.pop()]=""
        return "".join(lis)