class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        star = 0
        for edge in range(1,len(edges)):
            star = set(edges[edge - 1]).intersection(set(edges[edge]))
          
        return list(star)[0]