class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = Counter(s)
        updated = sorted(count.items() , key=lambda x:x[1])
        
        if updated[0][1] > 1:
            return -1
        
        for k,v in updated:
            if v == 1:
                return s.index(k)