
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        lower = defaultdict(list)

        connection = [0 for _ in range(length)]
        answer = [i for i in range(length)]

        queue = deque([])

        for a, b in richer:
            lower[a].append(b)
            connection[b] += 1

        for con in range(length):
            if connection[con] == 0:
                queue.append(con)
                answer[con] = con
                
        while queue:
            
            node = queue.popleft() 
            take = quiet[node]
            
            for ngh in lower[node]:
                if quiet[node] < quiet[ngh]: 
                    quiet[ngh] = take
                    answer[ngh] = answer[node] 
                connection[ngh] -= 1
                if connection[ngh] == 0:
                    queue.append(ngh)

        return answer