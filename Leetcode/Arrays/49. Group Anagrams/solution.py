class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        # Sort each strs[i] approach
        # Time: O(N * SlogS)
        # Space: O(N)
        anagramMap = {} # sorted string -> List of ALL corresponding anagrams

        for s in strs:
            sstr = "".join(sorted(s))

            # empty case
            if sstr not in anagramMap:
                anagramMap[sstr] = []

            anagramMap[sstr].append(s)

        return list(anagramMap.values())

class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        # Tuple as key approach
        # Time: O(N * S)
        # Space: O(N)
        anagramMap = {} # charCount -> strs[i]

        for s in strs:

            # count each characters 
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            charKey = tuple(charCount)

            if charKey not in anagramMap:
                anagramMap[charKey] = []

            anagramMap[charKey].append(s)

        # append all values into result 
        return list(anagramMap.values())
