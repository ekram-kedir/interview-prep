class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        answer = 0
        for cost in costs:
            cost.append((cost[1] - cost[0]))
            
        updated = sorted(costs , key = lambda x: x[2])
        length = len(costs) // 2
        
        for l in range(length):
            answer += updated[l][1]
            
        for l in range(length , len(costs)):
            answer += updated[l][0]

        return answer