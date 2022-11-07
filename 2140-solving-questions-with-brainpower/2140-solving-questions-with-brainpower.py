class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        l=len(questions)
        b=[0]*(l+1)
        for i,j in enumerate(questions):
            b[i+1]=max(b[i+1],b[i])
            x=min(i+j[1]+1,l)
            b[x]=max(b[x],b[i]+j[0])
        return b[l]