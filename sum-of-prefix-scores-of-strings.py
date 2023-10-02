class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            else:
                cur.children[word[i]].frequency += 1
            cur = cur.children[word[i]]
    
    def prefix(self,word):
        cur = self.root
        pre = 0
        for i in range(len(word)):
            if word[i] in cur.children:
                pre += cur.children[word[i]].frequency
            cur = cur.children[word[i]]
        return pre

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        arr = []
        for i in words:
            trie.insert(i)
        for i in words:
           pre = trie.prefix(i)
           arr.append(pre)

        return arr