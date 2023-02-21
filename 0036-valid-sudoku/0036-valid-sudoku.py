class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        ch1 = []
        ch2 = []
        ch3 = []
        answer = []
        def checkduplicate(n):
            result = True
            array = Counter(n)
            for k,v in array.items():
                if v > 1 and k != ".":
                    result = False
            return result
            
        for num in range(col):
            check1 = []
            for nums in range(row):
                check1.append(board[nums][num])
            checkduplicate(check1)
            answer.append(checkduplicate(check1))

        for num in range(row):
            check2 = []
            for nums in range(col):
                check2.append(board[num][nums])
            checkduplicate(check2)
            answer.append(checkduplicate(check2))
            
        diagonals = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        operations = [(0,1),(1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,-1),(-1,0),(0,0)]
        for row,col in diagonals:
            check3 = []
            for op1,op2 in operations:
                check3.append(board[row + op1][col + op2])
            checkduplicate(check3) 
            answer.append(checkduplicate(check3))
    
    
        for ans in answer:
            if False in answer:
                return False
            return True
        
            