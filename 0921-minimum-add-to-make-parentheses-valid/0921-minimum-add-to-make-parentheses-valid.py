class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        stack=0
        for i in s:
            if i=="(":
                stack+=1
            if stack>0 and i==")":
                stack-=1
            elif stack==0 and  i==")":
                count+=1
        return stack+count