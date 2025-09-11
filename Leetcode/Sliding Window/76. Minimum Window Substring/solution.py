class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time: O(len(s)) | Space: O(52)

        if len(s) < len(t): 
            return ""

        sCount = defaultdict(int)   # schar -> count
        tCount = defaultdict(int)   # tchar -> count

        for c in t:
            tCount[c] += 1

        matches, required = 0, len(tCount)
        l, res = 0, ""

        for r in range(len(s)):
            c = s[r]
            sCount[c] += 1

            if sCount[c] == tCount[c]:
                matches += 1
            # print(matches, required)
            while matches == required:
                # print(s[l:r+1])
                # updates res if needed
                if res == "" or len(res) >= (r - l + 1): 
                    res = s[l:r+1]

                if sCount[s[l]] == tCount[s[l]]:
                    matches -= 1
                sCount[s[l]] -= 1
                l += 1

        return res