class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
       
        while len(stones) > 1:
            first = -1 * heappop(stones)
            second = -1 * heappop(stones)
           
            if first > second:
                heappush(stones ,-1* (abs(first) - abs(second)))
                
        stones.append(0)
        return -1 * stones[0]