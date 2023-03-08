class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        target = max(arr)
        index = arr.index(target)
        return index
        
#         for num in range(index,len(arr)):
#             arr[num] += arr[num - 1]
        
#         left = -1
#         right = len(arr)
        
#         while left  + 1 < right:
#             mid = left + math.ceil((right - left)/2)
#             if arr[mid] < target:
#                 left = mid
#             else:
#                 right = mid
#         return right 
                
                