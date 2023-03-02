class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        left = 0
        right = 0
        count = 0
        
        while left < len(players) and right < len(trainers):
            
            if players[left] <= trainers[right]:
                count += 1
                left += 1
                right += 1
            elif players[left] > trainers[right]:
                right += 1
            else:
                break
        return count