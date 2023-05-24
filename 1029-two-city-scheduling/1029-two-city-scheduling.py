class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        
        for i in range(len(costs)):
            a,b = costs[i]
            difference.append(((a - b),i))
        difference.sort()
        
        total = 0
        half = len(costs)/2
        for i in range(len(costs)):
            if i < half:
                total += costs[difference[i][1]][0]
            else:
                total += costs[difference[i][1]][1]
            
        return total
        