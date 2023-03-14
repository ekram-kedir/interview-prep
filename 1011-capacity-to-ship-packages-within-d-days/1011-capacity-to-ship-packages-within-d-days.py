class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculate(weights,weight):
            total = 0
            day = 0
            for right in range(len(weights)):
                total += weights[right]
                while total >= weight:
                    if total == weight:
                        day += 1
                        total = 0
                    else:
                        day += 1
                        total = weights[right]
            if total > 0:
                day += 1
            return day

        left = max(weights)
        right = sum(weights)
 
        while right > left + 1:
            mid = left + (right - left)//2
            if calculate(weights, mid) > days:
                left = mid
            else:
                right = mid
             
        if calculate(weights, left) <= days and calculate(weights, right) < days:
            return left
        else:
            return right
    
