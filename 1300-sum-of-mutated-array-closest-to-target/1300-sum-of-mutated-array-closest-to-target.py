class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        left , right = 0, max(arr)
        result , answer = float("inf"), float("inf")
        while left <= right:
            mid =  (right + left) // 2
            total = 0
            for num in arr:
                total += min(mid , num)
            value = abs(total - target)
            if value == answer:
                result = min(result , mid)
            if value < answer:
                answer = value
                result = mid
            if total >= target:
                right = mid - 1
            else:
                left = mid + 1
        return result


       
        
        