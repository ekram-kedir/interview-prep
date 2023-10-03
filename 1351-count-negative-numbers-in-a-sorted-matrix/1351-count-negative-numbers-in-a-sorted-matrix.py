class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        for g in grid:
            length = len(g)
            for element in g:
                if element < 0:
                    count += 1
                    
        return count