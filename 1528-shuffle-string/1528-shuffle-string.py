class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        answer = ["" for i in range(len(s))]
        
        for index,ind in enumerate(indices):
            answer[ind] += s[index]
            
        return "".join(answer)