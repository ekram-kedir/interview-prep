class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        total = []
        for mat in matrix:
            total.extend(mat)
        
        heapify(total)
       
        count = 1
        
        while count < k:
            count += 1
            heappop(total)
            
        return heappop(total)