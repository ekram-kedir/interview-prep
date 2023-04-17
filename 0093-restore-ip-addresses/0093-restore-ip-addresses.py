class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        self.backtrack(s, [], results)
        return results
    
    def backtrack(self, s, curr, results):
        
        if len(curr) == 4 and not s:
            results.append('.'.join(curr))
            return
        
        if len(curr) == 4 or not s:
            return
        
        for i in range(1, min(4, len(s)+1)):
            if i > 1 and s[0] == '0':
                continue
            num = int(s[:i])
            if num > 255:
                continue
            curr.append(s[:i])
            self.backtrack(s[i:], curr, results)
            curr.pop()
        

