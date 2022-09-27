class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n=0,0
        ans=[]
        nums1.sort()
        nums2.sort()
        while m<len(nums1) and n<len(nums2):
            if nums1[m]<nums2[n]:
                m+=1
            elif nums2[n]<nums1[m]:
                n+=1
            elif nums2[n]==nums1[m]:
                ans.append(nums1[m])
                n+=1
                m+=1
        return ans