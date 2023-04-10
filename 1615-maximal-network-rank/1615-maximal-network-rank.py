class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        values = [set() for road in range(n)]
        
        for src,dest in roads:
            values[src].add(dest)
            values[dest].add(src)
       
        answer = 0
     
        for val in range(len(values)):
            for inner in range(val + 1,len(values)):
                common = len(values[val].intersection(values[inner]))
                if val in values[inner]:
                     answer = max(answer , (len(values[val].union(values[inner])) + common - 1))
                else:
                    answer = max(answer , (len(values[val].union(values[inner])) + common))

        return answer
       