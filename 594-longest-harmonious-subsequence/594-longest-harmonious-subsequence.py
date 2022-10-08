class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans=Counter(nums)
        res=0
        for i in ans:
            if i+1 in ans:
                res=max(res,ans[i]+ans[i+1])
        return res
            