class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        
        for i in zip(nums,index):
            a,b = i
            
            target.insert(b,a)
            
        return target