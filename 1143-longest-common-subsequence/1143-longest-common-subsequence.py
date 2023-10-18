class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        length_text1 = len(text1)
        length_text2 = len(text2)
        @cache
        def dp(index1,index2):
            
            if index1 >= length_text1 or index2 >= length_text2:
                return 0
            
            if text1[index1] == text2[index2]:
                return 1 + dp(index1 + 1, index2 + 1)
            return max(dp(index1, index2 + 1) , dp(index1 + 1, index2))
            
        return dp(0 , 0)
