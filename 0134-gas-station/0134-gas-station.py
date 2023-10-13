class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        length = len(gas)
        difference = 0
        answer = 0
        
        if sum(gas) < sum(cost):
            return -1
        
        for ind in range(length):
            difference += gas[ind] - cost[ind]
            if difference < 0:
                difference = 0
                answer = ind + 1
                
        return answer
                

      