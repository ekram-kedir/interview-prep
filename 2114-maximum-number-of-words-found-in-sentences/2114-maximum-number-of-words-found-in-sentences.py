class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_word = 0
        
        for word in sentences:
            max_word = max(len(str(word).split()) , max_word)
        return max_word