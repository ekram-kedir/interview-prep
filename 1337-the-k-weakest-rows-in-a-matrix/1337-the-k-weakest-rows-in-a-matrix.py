class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        dic = [[i, 0] for i in range(len(mat))]
        
        for m in range(len(mat)):
            dic[m][1] = mat[m].count(1)
            
        updated = sorted(dic , key = lambda x:x[1])
        answer = [k for k,v in updated]
        
        return answer[:k]
            