class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        check = 1
        
        if check & n == 1:
            n = n >> 1
        else:
            n = n
            
        checkAll = 2
        checkSecond = 3
        
        while n >= 1:
            if ((checkAll & n == checkAll) and (checkSecond & n == checkAll)) and checkAll | n == n:
                n = n >> 2
            else:
                return False
        return True
        