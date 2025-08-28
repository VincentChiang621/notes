def encode(self, strs:List[str]) -> str:
    # Format <length>#<strs[i]>
    # Time: O(n) | Space: O(n)
    res = ""
    # 1. loop strs and get each len(strs) + "#"
    for s in strs:
        # 2. add (len(strs) + "#") in front of each strs[i], append to res
        res += str(len(s)) + '#' + s
    return res

def decode(self, s:str) -> List[str]:
    # Time: O(n) | Space: O(n)
    res, i = [], 0

    while i < len(s):
        # 1. grab integer (before '#') to know length of strs[i]
        length = ''
        while s[i] != '#':
            length += s[i]
            i += 1

        # 2. skip '#' and get length of the string (we know length)
        out = s[i+1: i+1+int(length)]

        # 3. get str[i] index
        i = i + int(length) + 1
        res.append(out)

    return res