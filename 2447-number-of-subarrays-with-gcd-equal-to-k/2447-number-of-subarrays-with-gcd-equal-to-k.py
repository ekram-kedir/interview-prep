class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        count = 0
        for r in range(len(nums)):
            
           current = nums[r]
           for l in range(r, len(nums)):
                
                current = math.gcd(current , nums[l])
                if current == k:
                    count += 1
                elif current < k:
                    break
                    
        return count

