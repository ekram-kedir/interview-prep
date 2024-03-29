class RandomizedSet:

    def __init__(self):
        self.element = []
        
    def insert(self, val: int) -> bool:
        
        if val in self.element:
            return False
        else:
            self.element.append(val)
            return True

    def remove(self, val: int) -> bool:
        
        if val in self.element:
            self.element.pop(self.element.index(val))
            return True
        else:
            return False

    def getRandom(self) -> int:
        
        return random.choice(self.element)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()