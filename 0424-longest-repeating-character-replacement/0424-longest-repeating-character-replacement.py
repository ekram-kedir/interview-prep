class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans={}
        l=0
        count=0
        wi=0
        for r in range(len(s)):
            ans[s[r]]=1+ans.get(s[r],0)
            count=max(ans[s[r]],count)
            while (r-l+1)-count>k:
                ans[s[l]]-=1
                l+=1
            wi=max(wi,r-l+1)
        return wi
                