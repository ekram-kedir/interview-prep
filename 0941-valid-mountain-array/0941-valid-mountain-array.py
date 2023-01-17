class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start , end , count = 0 , -1 ,len(arr)
        
        while start < count - 1 and arr[start] < arr[start + 1]:
            start += 1
        while end > - count and arr[end] < arr[end - 1]:
            end -= 1
        
        return start == end + count and 0 < start and end < -1