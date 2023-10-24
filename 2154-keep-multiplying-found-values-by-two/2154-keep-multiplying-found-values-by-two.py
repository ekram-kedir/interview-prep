class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        check = original
        
        while check in nums:
            check *= 2
            
        return check