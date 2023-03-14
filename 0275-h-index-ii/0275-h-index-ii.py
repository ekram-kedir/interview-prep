class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = len(citations) 

        while left + 1 < right:
            
            mid = left + (right - left)//2
            
            if len(citations) - mid == citations[mid]: return citations[mid]
            if len(citations) - mid > citations[mid]: left = mid
            else: right = mid

        return len(citations) - right