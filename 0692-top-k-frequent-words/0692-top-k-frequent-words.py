class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        answer = []
        words_dic = Counter(words)
        words_heap = [(-v,k) for (k , v) in words_dic.items()]
        
        heapify(words_heap)
        count = 0
        
        while count < k:
            
            answer.append(heappop(words_heap)[1])
            count += 1
            
        return answer