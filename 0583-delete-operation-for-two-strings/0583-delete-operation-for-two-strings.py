class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        length_word1 = len(word1)
        length_word2 = len(word2)
        
        @cache
        def dp(index1,index2):

            if index1 >= length_word1:
                return length_word2 - index2
            if index2 >= length_word2:
                return length_word1 - index1
            
            if word1[index1] == word2[index2]:
                return dp(index1 + 1, index2 + 1)
            return min(dp(index1, index2 + 1) , dp(index1 + 1, index2)) + 1
            
        return dp(0 , 0)
