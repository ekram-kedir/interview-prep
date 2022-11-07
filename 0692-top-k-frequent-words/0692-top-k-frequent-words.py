class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        seen=Counter(words)
        minheap=[(-see,word) for word,see in seen.items()]
        heapq.heapify(minheap)
        ans=[]
        while k>0:
            ans.append(heappop(minheap)[1])
            k-=1
        return ans
