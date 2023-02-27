class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        take  = []
        for i in zip(*trips):
            take.append(i)
        n = max(take[-1])
        prefixSum = [0] * (n + 1)
       
        for passenger , start , end  in trips:
            
            prefixSum[start] += passenger
            
            prefixSum[end] -= passenger
        for prefix in range(1,len(prefixSum)):
            prefixSum[prefix] += prefixSum[prefix - 1]
            
        for prefix in prefixSum:
            if prefix > capacity:
                return False
        return True