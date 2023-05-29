class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        costVal = [i for i in range(n)]
        
        if n == 1:
            costVal[0] = cost[0]
            return cost[0]
        if n == 2:
            costVal[0] = cost[0]
            costVal[1] = cost[1]
            return min(costVal)
        if n == 3:
            costVal[0] = cost[0]
            costVal[1] = cost[1]
            costVal[2] = cost[2]
            return min(costVal[0] + costVal[2], costVal[1])
        else:
            costVal[0] = cost[0]
            costVal[1] = cost[1]
            for i in range(2,n):
                costVal[i] = min(costVal[i - 1],costVal[i -2]) + cost[i]
            return min(costVal[-1] , costVal[-2])
       
       
