class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        total = 0
        
        for left in range(len(arr)):
            right = 0
            while right < len(arr):
                if ((right - left + 1) % 2) != 0:
                    total += sum(arr[left:right + 1])
                right += 1
                
        return total