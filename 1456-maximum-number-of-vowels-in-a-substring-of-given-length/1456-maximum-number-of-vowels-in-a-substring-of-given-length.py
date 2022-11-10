class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        max_count = 0
        for ind,val in enumerate(s):
            if ind >= k:
                if s[ind-k] in "aeiou":
                    count -= 1
            if s[ind] in "aeiou":
                count += 1
            max_count=max(count,max_count)
        return max_count
        
                
                