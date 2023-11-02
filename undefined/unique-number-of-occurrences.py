class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count = Counter(arr)
        freq_count = count.values()
        
        if len(set(freq_count)) == len(freq_count):
            return True
        return False
