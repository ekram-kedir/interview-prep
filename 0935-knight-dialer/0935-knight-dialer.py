class Solution:
    def checkBoundary(self , row , col , row_length, col_length):
        
        if row < 0 or row >= row_length or col < 0 or col >= col_length:
            return True
        
        if (row == 3 and col == 0) or (row == 3 and col == 2):
            return True
        
        return False
    
    def knightDialer(self, n: int) -> int:
        dxn = [(2,-1) , (1,-2) , (2,1) , (1,2) , (-1,-2) , (-2,-1) , (-1,2) , (-2,1)]
        @cache
        def helper(r ,c , length):
            
            if self.checkBoundary(r, c, 4 , 3):
                return 0
            
            if length == n:
                return 1
            
            ans = 0
            for dr, dc in dxn:
                new_r = r + dr
                new_c = c + dc
                
                ans += helper(new_r , new_c , length + 1)
                
            return ans % ((10**9) + 7)
        
        answer= 0
        
        for row in range(4):
            for col in range(3):
                answer += helper(row , col , 1)
                
        return answer % ((10**9) + 7)
                
            