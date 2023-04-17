class Solution:
    def backtrack(self , index , subsequence , visited , arr):
        if len(subsequence) > 0 and subsequence in visited:
            return 0
        
        visited.add(subsequence)
        count = len(subsequence)
        for idx in range(index , len(arr)):
            if len(arr[idx]) != len(set(arr[idx])):
                continue
            if not set(arr[idx]).intersection(set(subsequence)):
                count = max(count , self.backtrack(idx + 1 , subsequence + arr[idx] , visited , arr))
        return count
    
    def maxLength(self, arr: List[str]) -> int:
        visited = set()
        return  self.backtrack(0 , "" , visited , arr)