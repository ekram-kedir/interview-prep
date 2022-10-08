class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxHeap=[-i for i in count.values()]
        heapq.heapify(maxHeap)
        time=0
        k=deque()
        while maxHeap or k:
            time+=1
            if maxHeap:
                i=1+heapq.heappop(maxHeap)
                if i:
                    k.append([i,time+n])
            if k and k[0][1]==time:
                heapq.heappush(maxHeap,k.popleft()[0])
        return time