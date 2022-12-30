class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordMap = {}
        
        for i in range(len(words)):
            for j in range(i + 1,len(words)):
                if Counter(words[i]).keys() == Counter(words[j]).keys():
                    wordMap[words[i]] = 1 + wordMap.get(words[i], 0)
                    
        return sum(wordMap.values())