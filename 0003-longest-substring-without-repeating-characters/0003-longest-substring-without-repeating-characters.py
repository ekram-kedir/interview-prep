class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        crossChecker = set()
        countTrack = 0
        start = 0
        
        for end in range(len(s)):
            
            while s[end] in crossChecker:
                crossChecker.remove(s[start])
                start += 1
            crossChecker.add(s[end])
            countTrack = max(end - start + 1, countTrack)
        
        return countTrack
            