class Solution:
    def numTeams(self, rating: List[int]) -> int:
            n = len(rating)
            
            if n < 3:
                return 0


            less = [0] * n
            greater = [0] * n

            for i in range(n):
                for j in range(i):
                    if rating[i] > rating[j]:
                        greater[i] += 1
                    elif rating[i] < rating[j]:
                        less[i] += 1

            total_teams = 0
            for i in range(n):
                for j in range(i):
                    if rating[i] > rating[j]:
                        total_teams += greater[j]
                    elif rating[i] < rating[j]:
                        total_teams += less[j]

            return total_teams


