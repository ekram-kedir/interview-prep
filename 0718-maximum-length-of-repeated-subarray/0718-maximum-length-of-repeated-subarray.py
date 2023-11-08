class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        max_length = 0

        for i in range(len(nums1)):
            max_length = max(max_length, self.check(nums1, nums2, i, 0))

        for j in range(len(nums2)):
            max_length = max(max_length, self.check(nums1, nums2, 0, j))

        return max_length

    def check(self, nums1, nums2, i, j):
        
        max_length = 0
        current_length = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
            i += 1
            j += 1

        return max_length