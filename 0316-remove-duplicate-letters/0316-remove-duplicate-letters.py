class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        crossChecker = set()
        countTrack = []
        count = Counter(s)

        for end in range(len(s)):
            
            if not s[end] in crossChecker: 
                while crossChecker and s[end] < countTrack[-1] and count[countTrack[-1]] > 0:

                    current  = countTrack.pop()
                    crossChecker.remove(current)
                
                countTrack.append(s[end])
                crossChecker.add(s[end])
            
            count[s[end]] -= 1
            
        return "".join(countTrack)
            