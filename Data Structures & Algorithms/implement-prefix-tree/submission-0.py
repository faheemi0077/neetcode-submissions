class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] in cur.children.keys():
                cur = cur.children[word[i]]
            else:
                cur.children[word[i]] = TrieNode()
                cur = cur.children[word[i]]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i] in cur.children.keys():
                cur = cur.children[word[i]]
            else:
                return False
        if cur.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] in cur.children.keys():
                cur = cur.children[prefix[i]]
            else:
                return False
        return True