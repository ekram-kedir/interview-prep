class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def helper(index , swap):
            
            answer = float("inf")
            
            if index == len(nums1) or index == len(nums2):
                return 0
        
            if swap:
                if (nums1[index - 1] < nums1[index] and nums2[index - 1] < nums2[index]):
                    answer = min(answer ,1 +  helper(index + 1 , True))
            
                if (nums2[index - 1] < nums1[index]) and (nums1[index - 1] < nums2[index]):
                    answer = min(answer , helper(index + 1 , False))
            else:
                
                if (nums1[index - 1] < nums1[index] and nums2[index - 1] < nums2[index]):
                    answer = min(answer ,helper(index + 1 , False))
            
                if (nums2[index - 1] < nums1[index]) and (nums1[index - 1] < nums2[index]):
                    answer = min(answer ,1 + helper(index + 1 , True))
                    

            return answer
        
        return min(1 + helper(1 , True) , helper(1 , False))