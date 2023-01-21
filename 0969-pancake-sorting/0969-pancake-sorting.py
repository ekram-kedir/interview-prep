class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res=[]
        
        def helper(idx):
            for i in range(0 , idx // 2 + 1):
                
                temp = A[i]
                A[i] = A[idx - i]
                A[idx - i] = temp
                
        for i in range( len(A) - 1, 0, - 1):
            for j in range(1,i + 1):
                if A[j] == i + 1:
                    helper(j)
                    res.append(j + 1)
                    break
            helper(i)
            res.append(i + 1)
        return res