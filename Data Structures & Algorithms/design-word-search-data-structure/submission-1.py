class Node():
    def __init__(self):
        self.children = {}
        self.word_end = False
class WordDictionary:
    def __init__(self):
        self.root = Node()
    def char_idx(self, c):
        return ord(c) - ord('a')

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = self.char_idx(c)
            if idx not in curr.children:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.word_end = True

    def search(self, word: str, curr = None) -> bool:
        curr = curr or self.root
        i = 0
        while i < len(word):
            c = word[i]
            if c == '.':
                suffix = word[i+1:]
                return any(
                    self.search(suffix, child) \
                    for child in curr.children.values()
                )
            else:

                idx = self.char_idx(c)
                if idx not in curr.children:
                    return False
                curr = curr.children[idx]
            i += 1
        return i == len(word) and curr.word_end
