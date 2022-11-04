class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        count_p=Counter(p)
        count_s=Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            count_s[s[i]]+=1
            if count_p==count_s:
                ans.append(i-len(p)+1)
            count_s[s[i-len(p)+1]]-=1
        return ans
 
         