class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        left = 0
        right = 0
        merged = []
        
        while left < len(word1) or right < len(word2):
             if left < len(word1) and right < len(word2):
                    merged.append(word1[left])
                    merged.append(word2[right])
                    left += 1
                    right += 1
                    
             elif left == len(word1) and right < len(word2):
                    merged.append(word2[right])
                    right += 1
                    
             elif right == len(word2) and left < len(word1):
                    merged.append(word1[left])
                    left += 1
                    
        return "".join(map(str,merged))