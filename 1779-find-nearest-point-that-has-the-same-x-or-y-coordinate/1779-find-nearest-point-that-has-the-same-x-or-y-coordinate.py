class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        shortDistance = float("inf")
        smallestIndex = -1
        
        for index,(a,b) in enumerate(points):
            if x == a or y == b:
                distance = abs(x - a) + abs(y - b)
                
                if shortDistance > distance:
                    shortDistance = distance
                    smallestIndex = index
        return smallestIndex
        
        
        
                 
            
        
            
            