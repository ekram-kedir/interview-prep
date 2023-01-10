class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        ans=[]
        start , end , left , right = 0, len(matrix), 0, len(matrix[0])
        
        while start < end or left < right:
            
            if start < end:
                ans.extend([matrix[start][i] for i in range (left,right)])
                start+=1
                
            if left < right:
                ans.extend([matrix[i][right-1] for i in range (start,end)])
                right-=1
                
            if start < end:
                ans.extend([matrix[end-1][i] for i in range (right-1,left-1,-1)])
                end-=1
                
            if left < right:
                ans.extend([matrix[i][left] for i in range (end-1,start-1,-1)])
                left+=1
                
        return ans
