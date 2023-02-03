class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans=0
        d={}
        for i in nums:
            y=k-i
            if y in d and d[y]>0:
                ans+=1
                d[y]-=1
            else:
                if i not in d:
                    d[i]=0
                d[i]+=1
        return ans