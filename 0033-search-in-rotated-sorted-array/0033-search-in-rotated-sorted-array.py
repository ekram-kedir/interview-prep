class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        store_the_idx = defaultdict(int)
        
        for idx,num in enumerate(nums):
            store_the_idx[num] = idx
            
        nums.sort()
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return store_the_idx[nums[mid]]
            
        return -1 