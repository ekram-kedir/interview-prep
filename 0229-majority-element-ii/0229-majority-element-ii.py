class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        cal = len(nums) / 3
        count = Counter(nums)
        
        answer = []
        if len(nums) == 1:
            return nums
        else:
            for k , v in count.items():
                if v > cal:
                    answer.append(k)
            return answer
                