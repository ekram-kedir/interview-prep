class MyHashSet:

    def __init__(self):
        self.array= [-1] * pow(10 , 7)

    def add(self, key: int) -> None:
        self.array[key] = 0

    def remove(self, key: int) -> None:
        self.array[key] = -1

    def contains(self, key: int) -> bool:
        if self.array[key] == 0:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)