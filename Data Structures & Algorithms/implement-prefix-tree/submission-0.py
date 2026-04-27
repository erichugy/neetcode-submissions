class Node:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False
class PrefixTree:
    def __init__(self):
        self.root = Node()

    def pos(self, c):
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            pos = self.pos(c)
            if not curr.children[pos]:
                curr.children[pos] = Node()
            curr = curr.children[pos]
        curr.word_end = True

    def search(self, word: str) -> bool:
        i = 0 
        curr = self.root
        while i < len(word):
            pos = self.pos(word[i])
            if curr.children[pos]:
                curr = curr.children[pos]
            i += 1
        return i == len(word) and curr.word_end
            
    def startsWith(self, prefix: str) -> bool:
        i = 0 
        curr = self.root
        while i < len(prefix):
            pos = self.pos(prefix[i])
            if not curr.children[pos]:
                return False
            curr = curr.children[pos]
            i += 1
        return True