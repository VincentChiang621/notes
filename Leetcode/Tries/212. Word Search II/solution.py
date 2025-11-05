# SOLUTION 1
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Brute Force
        # Time: O(n * m * 4^L * L = len(words))
        m, n = len(board), len(board[0])

        def dfs(r, c, word, idx, visited):
            if idx == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n):
                return False
            if board[r][c] != word[idx] or (r, c) in visited:
                return False

            visited.add((r, c))
            found = (
                dfs(r + 1, c, word, idx + 1, visited)
                or dfs(r - 1, c, word, idx + 1, visited)
                or dfs(r, c + 1, word, idx + 1, visited)
                or dfs(r, c - 1, word, idx + 1, visited)
            )
            visited.remove((r, c))
            return found

        def exists(word):
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, word, 0, set()):
                        return True
            return False
        
        return [w for w in words if exists(w)]
    
# SOLUTION 2
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Prefix Tree to help with pruning
        # Time: O(n * m * 4^L) | Space O(N) N=letters in TrieNode

        def buildTree(): 
            for w in words:
                cur = self.root
                for c in w:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()

                    cur = cur.children[c]

                cur.end = True
                cur.word = w
        
        # 1. built prefix tree of `words`
        buildTree()

        # 2. check each char on the board
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, cur, visited):
            if cur.end:
                nonlocal res
                res.add(cur.word)

            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            elif board[r][c] not in cur.children:
                return
            elif (r,c) in visited:
                return
            

            visited.add((r,c))
            cur = cur.children[board[r][c]]

            down = backtrack(r + 1, c, cur, visited)
            up = backtrack(r - 1, c, cur, visited)
            right = backtrack(r, c + 1, cur, visited)
            left = backtrack(r, c - 1, cur, visited)

            visited.remove((r,c))

            return

        res = set()
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, self.root, set())

        return list(res)