class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQue = deque()
        minQue = deque()
        
        left = 0
        maxLength = 0
        for right  in range(len(nums)):
            while maxQue and nums[right] > nums[maxQue[-1]]:
                maxQue.pop()
            maxQue.append(right)
            
            while minQue and nums[right] < nums[minQue[-1]]:
                minQue.pop()
            minQue.append(right)
            
            while left < right and nums[maxQue[0]] - nums[minQue[0]] > limit:
                if left == maxQue[0]:
                    maxQue.popleft()
                elif left == minQue[0]:
                    minQue.popleft()
                left += 1
            
            
            maxLength = max(maxLength , right - left + 1)
        return maxLength