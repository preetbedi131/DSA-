class MyHashSet:

    def __init__(self):
        self.size=1024
        self.bucket=[[] for i in range(self.size)]

    def _hash(self,key:int):
      return hash(key)%self.size

    def add(self, key: int) -> None:
        i = self._hash(key)
        if key not in self.bucket[i]:#for unique entris
              self.bucket[i].append(key)

    def remove(self, key: int) -> None:
        i = self._hash(key)
        if key in self.bucket[i]:
            self.bucket[i].remove(key)
        

    def contains(self, key: int) -> bool:
        i = self._hash(key)
        return key in self.bucket[i]

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
