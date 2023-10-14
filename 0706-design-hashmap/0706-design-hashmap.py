class MyHashMap:

    def __init__(self):
        self.array = []

    def put(self, key: int, value: int) -> None:
        
        if len(self.array) == 0:
            self.array.append([key , value])
        else:
            for index , element in enumerate(self.array):
                k , v = self.array[index]
                if k == key:
                    self.array[index] = [key , value]
    
            if [key , value] not in self.array:
                self.array.append([key , value])
                
    def get(self, key: int) -> int:
        if len(self.array) > 0:
            for k,v in self.array:
                if key == k:
                    return v
            return -1
        return -1
    def remove(self, key: int) -> None:
        if len(self.array) > 0:
            for index , element in enumerate(self.array):
                k , v = self.array[index]
                if k == key:
                    self.array.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)