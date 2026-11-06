class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.data.append(key)
        return
        
    def remove(self, key: int) -> None:
        for index in range(len(self.data)):
            if self.data[index] == key:
                self.data.pop(index)
                return 


    def contains(self, key: int) -> bool:
        for index in self.data:
            if index == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)