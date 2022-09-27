class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half=len(nums)/2
        count=0
        maj=Counter(nums)
        for k,v in maj.items():
            if v>=half:
                return k
        