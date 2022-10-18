class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans=0
        begn,end=0,1
        if k==0:
                dup=Counter(nums)
                return sum(dup[i]>1 for i in dup)
        nums=sorted(list(set(nums)))
        while end<len(nums):
            diff=abs(nums[begn]-nums[end])
            
            if diff==k:
                ans+=1
                begn+=1
                end=begn+1
            elif diff<k:
                end+=1
            else:
                begn+=1
                end=begn+1
        return ans