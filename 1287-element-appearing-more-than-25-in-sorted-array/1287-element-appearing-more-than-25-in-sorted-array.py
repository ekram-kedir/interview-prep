class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        
        for k,v in count.items():
            if v > (len(arr)//4):
                return k 