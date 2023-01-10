class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        rows = []
        before = []
        cols = []
        count = 0
        
        for i in range(len(grid)):
            res = ""
            for j in range(length):
                res += str(grid[i][j]) + "+" 
            rows.append(res[:-1])

        for i in zip(*grid):
            before.append(i)
        
        for i in range(len(before)):
            num = "+".join(map(str,before[i]))
            cols.append(num)
      
       
        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] == cols[j]:
                    count += 1
                    
        return count