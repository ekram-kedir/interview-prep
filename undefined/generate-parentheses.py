class Solution:
    def backtracking(self , opened_count , closed_count , n , result):
        
        if opened_count == closed_count == n:
            self.answer.append("".join(result))
            
        if opened_count < n:
            result.append("(")
            self.backtracking(opened_count + 1 , closed_count , n , result)
            result.pop()
            
        if closed_count < opened_count:
            
            result.append(")")
            self.backtracking(opened_count , closed_count + 1, n , result)
            result.pop()
            
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.answer = []
        self.backtracking(0 , 0, n , [])
        return self.answer