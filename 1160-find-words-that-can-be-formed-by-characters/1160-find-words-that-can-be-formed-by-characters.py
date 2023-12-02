class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count = 0
        count_chars = Counter(chars)
        
        for word in words:
            count_word = Counter(word)
            we_can = True
            for k,v in count_word.items():
                if not count_chars[k] or (count_chars[k] and v > count_chars[k]):
                    we_can = False
                    
            if we_can:
                count += len(word)
                
        return count