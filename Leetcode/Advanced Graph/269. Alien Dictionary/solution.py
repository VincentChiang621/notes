class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return "".join(set(words[0]))

        unique = set()
        for c in words[-1]:
            unique.add(c)
            
        inDegrees = {}
        frees = defaultdict(set)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            # track all unique + initialize hashmaps
            for c in w1 + w2:
                if c not in inDegrees:
                    inDegrees[c] = 0
                if c not in frees:
                    frees[c] = []
                unique.add(c)

            # initialize inDegrees & freeMap for Topological Sorting
            ind = 0
            for ind in range(min(len(w1), len(w2))):
                a, b = w1[ind], w2[ind]
                if a == b:
                    continue
                else:
                    if b not in frees[a]:
                        inDegrees[b] += 1
                        frees[a].append(b)
                    break

            if len(w1) > len(w2) and ind == len(w2) - 1 and w1[ind] == w2[ind]:
                return ""

        # Topological Sorting:
        q = deque()
        visited = set()
        for n in inDegrees:
            if inDegrees[n] == 0:
                q.append(n)

        res = ""
        while q:
            cur = q.popleft()

            if cur in visited:
                continue

            visited.add(cur)
            res += cur

            for n in frees[cur]:
                inDegrees[n] -= 1

                if inDegrees[n] == 0:
                    q.append(n)

        return res if len(res) == len(unique) else ""

            
