class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        answer = numBottles
        a = numBottles // numExchange
        b = numBottles % numExchange
        total = a + b
        
        while total >= numExchange:
            answer += a  
            a = total // numExchange
            b = total % numExchange
            total = a + b
        return answer + a