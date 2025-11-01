class TreeNode:
    def __init__(self):
        self.hmap = {}    # maps nextLetter -> address

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        # insert c into hmap (make new node if not exist)
        # update cur
        cur = self.root
        for c in word:
            if c not in cur.hmap:
                cur.hmap[c] = TreeNode()
            
            cur = cur.hmap[c]
        
        cur.hmap[" "] = None # indicates end of a word

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.hmap:
                return False
            cur = cur.hmap[c]

        return " " in cur.hmap

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.hmap:
                return False
            cur = cur.hmap[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)