class MyHashSet:

    def __init__(self):
        self.size=769
        self.buckets=[]
        for i in range(self.size):
            self.buckets.append([])
    
    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        h = self.hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self.hash(key)
        for i, data in enumerate(self.buckets[h]):
            if key == data:
                self.buckets[h].pop(i)
                break


    def contains(self, key: int) -> bool:
        h =self.hash(key)
        for data in self.buckets[h]:
            if data==key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)