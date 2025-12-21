class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        res = []
        def backtrack(comb, ind):
            if ind == len(digits):
                res.append(comb)
                return

            num = digits[ind]
            for let in letters[num]:
                backtrack(comb + let, ind + 1)

        backtrack("", 0)
        return res