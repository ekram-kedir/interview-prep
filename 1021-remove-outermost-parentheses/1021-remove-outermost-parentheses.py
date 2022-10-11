class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        count=0
        for i in s:
            if i=="(" and count!=0:
                stack.append(i)
                count+=1
            elif i==")" and count!=1:
                stack.append(i)
                count-=1
            elif i=="(" and count==0:
                count+=1
            else:
                count-=1

        return "".join(stack)