class MyHashMap: 
    def __init__(self):
      self.n = 1024
      self.array = [[] for _ in range(self.n)]
    
    def _hash(self, key):
      return hash(key) % self.n
  
    def put(self, key: int, value: int) -> None:   
      i = self._hash(key)
      bucket=self.array[i]
      for idx , (k,v) in enumerate(bucket):
        if k==key:
            bucket[idx]=(key,value)
            return
      bucket.append((key,value))

    def get(self, key: int) -> int:
      i = self._hash(key)
      bucket=self.array[i]
      for (k,v) in bucket:
        if k == key:
            return v
      return -1

        
    def remove(self, key: int) -> None:
      i = self._hash(key)
      bucket=self.array[i]
      for idx , (k,v) in enumerate(bucket):
        if k==key:
            bucket.pop(idx)
            return
      
      
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
