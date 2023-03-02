class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        left = 0
        right = 0

        while left < len(word1) and right < len(word2):
            if word1[left:] >= word2[right:]:
                merge += word1[left]
                left += 1
            else:
                merge += word2[right]
                right += 1
        while left < len(word1):
            merge += word1[left]
            left += 1
        while right < len(word2):
            merge += word2[right]
            right += 1
        return merge