class Node():
    def __init__(self , val = None):
        
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        
        self.head = Node(0)
        self.size = 0
        
    def get(self, index: int) -> int:
        
        if index >= self.size or index < 0:
            return -1
        
        current = self.head
        
        for node in range(index + 1):
            current = current.next
            
        return current.val
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size: 
            return
        self.size += 1
        current = self.head
        
        for node in range(index):
            current = current.next
        new = Node(val)
        
        new.next = current.next
        
        current.next = new
    def addAtHead(self, val: int) -> None:
      
        self.addAtIndex(0 ,val)
        
    def addAtTail(self, val: int) -> None:
        
        self.addAtIndex(self.size, val)

    
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index >= self.size or index < 0:
            return
        
        self.size -= 1
        current = self.head
        
        for node in range(index):
            current = current.next
        current.next = current.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)