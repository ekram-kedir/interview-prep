class Solution:
    def countPoints(self, rings: str) -> int:
        
        answer = defaultdict(list)
        
        for i in range(1,len(rings)):
            if i % 2 != 0:
                answer[int(rings[i])].append(rings[i - 1])
                
        count = 0
        for v in answer.values():
            if len(set(v)) == 3:
                count += 1
        return count