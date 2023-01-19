class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
            answer=[]
            count=[]
            for i in nums:
                for j in range(1,len(nums)+1):
                    if i>nums[j-1]:
                        count.append(nums[j-1])
                answer.append(len(count))
                count=[]
            return answer
                    
