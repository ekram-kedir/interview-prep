class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        arr.sort()
        last=(n*5)/100
        first=(n*5)/100       
        while last>0:
            arr.pop()
            last-=1
        while first>0:
            arr.pop(0)
            first-=1
        return float(sum(arr)/len(arr))