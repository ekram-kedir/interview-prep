class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        incoming = defaultdict(int)
        result = []
        
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                
        
        queue = deque(supplies)
        
        for s in range(len(supplies)):
            incoming[supplies[s]] = 0
        for r in range(len(recipes)):
            incoming[recipes[r]] += len(ingredients[r])
            
        
        while queue:
            
            ingr = queue.popleft()
            
            for val in graph[ingr]:
                incoming[val] -= 1
                if incoming[val] == 0:
                    queue.append(val)
                
        for r in range(len(recipes)):
            if incoming[recipes[r]] == 0:
                result.append(recipes[r])

        return result