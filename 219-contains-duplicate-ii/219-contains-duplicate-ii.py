class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums))==len(nums): return False  
        for i in range(len(nums)-k+2):
            window = nums[i:i+k+1]
            if len(set(window))<len(window): 
                return True
        return False

        