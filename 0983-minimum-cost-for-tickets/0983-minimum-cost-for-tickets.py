class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(index , min_cost):
            
            if index >= len(days):
                return min_cost
           
            week = index
            while week < len(days) and days[week] < days[index] + 7:
                week += 1
                
            month = index
            while month < len(days) and days[month] < days[index] + 30:
                month += 1
                
            min_cost = min(dp(month , min_cost + costs[2]), dp(index + 1 , min_cost + costs[0]) , dp(week , min_cost + costs[1]))   
                
            return min_cost
            
        return dp(0 , 0)   