class MyHashMap:

    def __init__(self):
        self.size = 10**6
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = []
        for i, (existing_key, _) in enumerate(self.buckets[index]):
            if existing_key == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        if self.buckets[index]:
            for existing_key, value in self.buckets[index]:
                if existing_key == key:
                    return value
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if self.buckets[index]:
            for i, (existing_key, _) in enumerate(self.buckets[index]):
                if existing_key == key:
                    del self.buckets[index][i]
                    return