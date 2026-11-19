class MyHashMap:

    def __init__(self):
        self.size=769
        self.bucket=[]
        for i in range(self.size):
            self.bucket.append([])

    def _hash(self,key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)

        for i, data in enumerate(self.bucket[h]):
            if data[0] == key:
                self.bucket[h][i][1]=value
                return

        self.bucket[h].append([key, value])
        

    def get(self, key: int) -> int:
        h=self._hash(key)

        for i, data in enumerate(self.bucket[h]):
            if data[0] == key:
                return data[1]
        
        return -1

    def remove(self, key: int) -> None:
        h=self._hash(key)
        print(self.bucket[h])

        for i, data in enumerate(self.bucket[h]):
            if data[0] == key:
                self.bucket[h].pop(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)