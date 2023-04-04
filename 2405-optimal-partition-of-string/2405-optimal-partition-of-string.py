class Solution:
    def partitionString(self, s: str) -> int:
        
        visited = set()
        count = 0
        
        for val in range(len(s)):
            if s[val] in visited:
                count += 1
                visited = set()
                visited.add(s[val])
            else:
                visited.add(s[val])
        return count + 1