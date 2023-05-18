class UnionFind:
    
    def __init__(self, size):
        
        self.root = [i for i in range(size)]
        
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
    def pr(self):
        return self.root 
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        length = len(s)
        answer = ["q"] * length
        f = UnionFind(length)
        for a,b in pairs:
            f.union(a,b)
        
        parent = defaultdict(list)
        index = defaultdict(list)
        result = f.pr()
        
        for i in range(len(result)):
            root = f.find(i)
            parent[root].append(s[i])
            index[root].append(i)
        
        for k,v in parent.items():
            v.sort(reverse = True)
            for val in index[k]:
                answer[val] = v.pop()
            
        return "".join(answer)
        