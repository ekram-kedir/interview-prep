class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
       
        for i in range(len(nums)):
            ans = ""
            ans += str(nums[i])
            
            if len(ans) == 1:
                nums.append(nums[i])
                
            elif len(ans) > 1:
                ans = ans[::-1]
                nums.append(int(ans))
                
        calculate = set(nums)
        return len(list(calculate))
    