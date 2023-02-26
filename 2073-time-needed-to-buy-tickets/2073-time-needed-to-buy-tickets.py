class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        for ticket  in range(len(tickets)):
            if tickets[ticket] < tickets[k]:
                total += tickets[ticket]
            else:
                if ticket > k:
                    total += tickets[k] - 1
                else:
                    total += tickets[k]
        return total 
                