class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            left = 0
            right = max(piles) 
            while right > left + 1:
                mid = left + (right - left)//2
                remain = 0
                for hour in range(len(piles)):
                    if piles[hour] <= mid:
                        remain += 1
                    else:
                        remain += math.ceil(piles[hour] / mid)
                if remain <= h:
                    right = mid
                else:
                    left = mid
                    
            return right