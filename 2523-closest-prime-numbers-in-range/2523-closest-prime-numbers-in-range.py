class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        answer = [-1 , -1]
        arr = [True for i in range(right+ 1)]
        arr[0] = arr[1] = False
        for j in range(right + 1):
            if arr[j]:
                for k in range(j * j , right + 1 , j):
                    arr[k] = False
        
        prime = []
        for j in range(left , right + 1):
            if arr[j]:
                prime.append(j)
        
        diff = defaultdict(list)
        for i in range(len(prime) - 1):
             diff[prime[i + 1] - prime[i]].append((prime[i],prime[i + 1]))
        sortedDiff = sorted(diff.items(),key=lambda x:x[0])
        
        if len(sortedDiff) >= 1 and len(sortedDiff[0][1]) >= 1:
            answer = sortedDiff[0][1][0]
            return answer
        return answer
        
        
        
        
        
        
        

        