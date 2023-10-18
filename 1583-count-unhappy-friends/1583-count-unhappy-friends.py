class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        rank = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        
        for index in range(len(preferences)):
            for element in range(len(preferences[index])):
                rank[index][preferences[index][element]] = element
                
        for index1 in range(len(pairs)):
            key1, val1 = pairs[index1]
            x_found = False
            y_found = False
            for index2 in range(len(pairs)):
                key2,val2 = pairs[index2]
                if key1 != key2 and val1 != val2:
                    if not x_found and  ((rank[key1][val1] > rank[key1][key2] and rank[key2][key1] < rank[key2][val2]) or (rank[key1][val2] < rank[key1][val1] and rank[val2][key1] < rank[val2][key2])):
                        x_found = True
                        count += 1
                    if not y_found and  ((rank[val1][key2] < rank[val1][key1] and rank[key2][val1] < rank[key2][val2]) or (rank[val1][val2] < rank[val1][key1] and rank[val2][val1] < rank[val2][key2])):
                        y_found = True
                        count += 1
                    
        return count
    
    