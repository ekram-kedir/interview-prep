class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        numbers_heap = [-p for p in piles]
        count = 0
        
        heapify(numbers_heap)
        
        while count < k:
            
            count += 1
            num = heappop(numbers_heap)
            num = floor(num / 2)
            heappush(numbers_heap , num)
      
        total = sum(numbers_heap)
        return -1 * total