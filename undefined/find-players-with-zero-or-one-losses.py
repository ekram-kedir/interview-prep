class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = []
        losers = defaultdict(int)
        
        for w, l in matches:
            winners.append(w)
            losers[l] += 1
            
        answer = [[],[]]
        
        answer[0] = (list(set(winners) - set(losers.keys())))
        for num in losers.keys():
            if losers[num] == 1:
                answer[1].append(num)
                
        answer[0].sort()
        answer[1].sort()
        return answer