class DataStream:

    def __init__(self, value: int, k: int):
        
        self.queue = collections.deque()
        self.value = value
        self.k = k
        self.counter = collections.Counter()

    def consec(self, num: int) -> bool:
        
        self.queue.append(num)
        if num == self.value:
            self.counter[num] += 1
            
        while len(self.queue) > self.k:
            pop = self.queue.popleft()
            self.counter[pop] -= 1
            if self.counter[pop] == 0:
                del self.counter[pop]
                
        return self.counter[self.value] == self.k
            
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
