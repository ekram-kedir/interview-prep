class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        store = {}
        for i in range(len(arr) - 1 , -1, -1):
            if arr[i] + difference in store:
                store[arr[i]] = store[arr[i] + difference] + 1
            else:
                store[arr[i]] = 1
        return max(store.values())
            
                
                
            
        