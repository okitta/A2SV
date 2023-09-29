class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_of_word = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.is_end_of_word

class Solution:
    def longestWord(self, words):
        trie = Trie()
        longest = ""
        words.sort()
        
        for word in words:
            trie.insert(word)
            if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                if all(trie.search(word[:i]) for i in range(1, len(word))):
                    longest = word

        return longest