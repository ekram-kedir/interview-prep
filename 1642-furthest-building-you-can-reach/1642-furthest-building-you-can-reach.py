class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jumps = []
        
        for i in range(1,len(heights)):
            if heights[i - 1] >= heights[i]:
                continue
        
            heappush(jumps,(heights[i] - heights[i - 1]))
            total = 0
            if len(jumps) > ladders:
                total += heappop(jumps)
                bricks -= total
            if bricks < 0:
                return i - 1
        return  len(heights) - 1
                    
                    