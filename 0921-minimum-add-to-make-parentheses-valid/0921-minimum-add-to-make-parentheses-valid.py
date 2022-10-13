class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
            if stack and i==")":
                stack.pop()
            elif len(stack)==0 and  i==")":
                count+=1
        return len(stack)+count