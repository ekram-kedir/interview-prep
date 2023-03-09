class Solution:
    def splitString(self, s: str) -> bool:
        l = len(s)
        result = []
        
        def helper(start):
            if start >= l :
                return len(result) >= 2
            
            for string in range(start , l):
                take = int(s[start:string + 1])
                if len(result) == 0 or take == result[-1] - 1:
                   result.append(take)
                   if helper(string + 1):
                        return True
                   result.pop()
                
                
            return False
        
        return helper(0)
                
                
        
        