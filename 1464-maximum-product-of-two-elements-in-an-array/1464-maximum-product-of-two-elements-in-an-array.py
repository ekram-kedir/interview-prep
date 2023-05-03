class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numbers = [-n for n in nums]
        heapq.heapify(numbers)
        first = -1 * heappop(numbers)
        second = -1 * heappop(numbers)
    
        
        return (first - 1) * (second - 1)