class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                sums=nums[i]+nums[j]+nums[k]
                if sums<0:
                    j+=1
                elif sums>0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return ans