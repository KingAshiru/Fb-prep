class WordDictionary:

    def __init__(self):
        self.dic = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dic[len(word)].add(word)

    def search(self, word: str) -> bool:
        k = len(word)
        if k not in self.dic:
            return False
        for wrd in self.dic[k]:
            i = 0
            while i < k and (word[i] == wrd[i] or word[i] == "."):
                i += 1
            if i == k:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
