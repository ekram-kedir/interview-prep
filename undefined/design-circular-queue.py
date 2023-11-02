class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [-1] * (k + 1)
        self.k = k
        self.front = 0
        self.rare = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que[self.rare] = value
        self.rare += 1
        self.rare %= (self.k + 1)
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.que[self.front] = -1
        self.front += 1
        self.front %= (self.k + 1) 
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.rare - 1]

    def isEmpty(self) -> bool:
        if self.rare - self.front == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if (self.rare + 1) % (self.k + 1) == self.front:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()