class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dictionary = {}
        

    def insert(self, key: str, val: int) -> None:
        print(self.dictionary)
        diff = val
        if key in self.dictionary:
            diff = val - self.dictionary[key]
        self.dictionary[key] = val
        cur = self.root
        for i in key:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur.children[i].prefix += diff
            cur = cur.children[i]


    def sum(self, prefix: str) -> int:
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        return cur.prefix

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)