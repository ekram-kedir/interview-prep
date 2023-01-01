class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        
        evenSum = sum(i for i in nums if i%2 == 0)
    
        for value , index in queries:
            
            if nums[index] % 2 == 0:
                evenSum -= nums[index]
            nums[index] += value 
            if nums[index] % 2 == 0:
                evenSum += nums[index]
                
            ans.append(evenSum)
            
        return ans