class TrieNode:
    def __init__(self):
        self.children = {}
        self.maxIdx = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word,index):
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
            cur.maxIdx = index
    
    def startWith(self,word):
        cur = self.root
        for i in word:
            if i not in cur.children:
                return -1
            cur = cur.children[i]
        return cur.maxIdx

    

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for idx,word in enumerate(words):
            new_word = word + "#" + word
            for i in range(len(word)):
                self.trie.insert(new_word[i:],idx)
        

    def f(self, pref: str, suff: str) -> int:
        return self.trie.startWith(suff + "#" + pref)
        



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)