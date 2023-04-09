class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        degrees = defaultdict(list)
        outDegree = set()
        inDegree = set()
        
        for edge in range(len(edges)):
            degrees[edges[edge][0]].append(edges[edge][1])
        
        for k,v in degrees.items():
            outDegree.add(k)
            for val in v:
                inDegree.add(val)
                
        common = outDegree.intersection(inDegree)
        answer = outDegree - common
        
        return list(answer)