class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adjMat = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                seq = word[:i] + '*' + word[i+1:]
                adjMat[seq].append(word)

        def bfs():
            q = deque([beginWord])
            level = 0
            seen = set()

            while q:
                level += 1
                for i in range(len(q)):
                    cur = q.popleft()

                    if cur in seen:
                        continue
                    elif cur == endWord:
                        return level
                    
                    seen.add(cur)

                    for i in range(len(cur)):
                        seq = cur[:i] + '*' + cur[i+1:]
                        q.extend(adjMat[seq])

            return 0 

        return bfs()
        

                