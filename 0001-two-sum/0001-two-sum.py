class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store_the_complement = {}
        
        for index,num in enumerate(nums):
            complement = target - num
            if num in store_the_complement:
                return [store_the_complement[num] , index]
            
            store_the_complement[complement] = index
        print(store_the_complement)