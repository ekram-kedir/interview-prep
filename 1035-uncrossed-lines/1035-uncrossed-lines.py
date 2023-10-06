class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def helper(indx1 , indx2 , count):
            
            if indx1 == len(nums1):
                return count
            
            if indx2 == len(nums2):
                return count
            
            if nums1[indx1]  == nums2[indx2]:
                
                pick = helper(indx1 + 1 , indx2 + 1 , count + 1)
                dont_pick = helper(indx1 + 1, indx2 + 1 , count)
                
                return max(pick , dont_pick)
            
            if nums1[indx1] != nums2[indx2]:
                p1 = helper(indx1 + 1 , indx2 , count)
                p2 = helper(indx1 , indx2 + 1 , count)
                
                return max(p1 , p2)
                
            return count
                
        
        return helper(0 , 0 , 0)
                