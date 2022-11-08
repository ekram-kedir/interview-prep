class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l,r=0,0
        seen={c:ind for ind,c in enumerate(s)}
        ans=[]
        for ind,c in enumerate(s):
            r=max(r,seen[c])
            if ind==r:
                ans.append(r-l+1)
                l=r+1
        return ans
                
        