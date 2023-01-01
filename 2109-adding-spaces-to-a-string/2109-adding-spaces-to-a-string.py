class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        res = []
        pointer = 0
        for space in spaces:
            res.append(s[pointer:space])
            pointer = space
        res.append(s[space:])
       
        return " ".join(res)