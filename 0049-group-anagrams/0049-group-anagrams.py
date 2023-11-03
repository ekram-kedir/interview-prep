class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            s=str(sorted(i))
            if s in ans:
                ans[s].append(i)
            else:
                ans[s]=[i]
        return list(ans.values())