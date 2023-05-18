class UnionFind:
    
    def __init__(self):
        
        self.root = [i for i in range(26)]
        
    def find(self , row):
        
        if row == self.root[row]:
            return row
        self.root[row] = self.find(self.root[row])
        return self.root[row]
    
    def union(self , row , col):
        root_row = self.find(row)
        root_col = self.find(col)
        
        if root_row != root_col:
            if root_row > root_col:
                self.root[root_row] = root_col
            elif root_col > root_row:
                self.root[root_col] = root_row
            else:
                self.root[root_col] = root_row

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        f = UnionFind()
        
        for equation in equations:
            first = equation[0]
            second = equation[3]
            if equation[1] == '=':
                f.union(ord(first) - 97 , ord(second) - 97)
        
            elif equation[1] == '!':
                continue
                
        for equation in equations:
            first = equation[0]
            second = equation[3]
            if equation[1] == '!' and f.find(ord(first) - 97) == f.find(ord(second) - 97):
                return False
        return True