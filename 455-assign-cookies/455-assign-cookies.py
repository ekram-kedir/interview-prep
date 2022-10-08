class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        a,b=0,0
        count=0
        while a<len(g) and b<len(s):
            if g[a]==s[b] or s[b]>=g[a]:
                count+=1
                a+=1
                b+=1
            elif g[a]>s[b]:
                b+=1
        return count
            