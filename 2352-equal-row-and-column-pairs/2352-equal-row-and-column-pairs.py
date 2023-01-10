class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        l = []
        k = []
        for i in range(len(grid)):
            res = ""
            for j in range(length):
               res += str(grid[i][j]) + "+" 
            l.append(res[:-1])
        print(l)
        
        r = []
        n = []
        for i in zip(*grid):
            r.append(i)
        print(r)
        for i in range(len(r)):
            s = "+".join(map(str,r[i]))
            n.append(s)
        print(n)
        
        
        count = 0
        for i in range(len(l)):
            for j in range(len(n)):
                if l[i] == n[j]:
                    count += 1
                    
        return count