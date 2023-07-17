class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=sum(nums[:3])
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            while j<k:
                sums=nums[i]+nums[j]+nums[k]
                if abs(sums-target)<abs(ans-target):
                    ans=sums
                if sums<target:
                    j+=1
                else: 
                    k-=1
        return ans