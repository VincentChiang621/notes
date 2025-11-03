class TrieNode:
    def __init__(self):
        self.charMap = {}
        self.end = False
        
class WordDictionary:
    def __init__(self):
       self.root = TrieNode()
 
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.charMap:
                cur.charMap[c] = TrieNode()

            cur = cur.charMap[c]

        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for val in node.charMap.values():
                        if dfs(i + 1, val):
                            return True
                    return False
                else:
                    if word[i] not in node.charMap:
                        return False
                    node = node.charMap[word[i]]

            return node.end

        return dfs(0, self.root)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)