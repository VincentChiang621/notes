class Solution:
    def isValidSudoku(self, board:List[List[int]]) -> bool:
        # N = len(board)
        # Time: O(N^2) | Space: O(N^2)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = board[r][c]
                if cur != ".":
                    ind = 3 * (r // 3) + (c // 3)
                    # check for duplicate digits
                    if cur in rows[r] or cur in cols[c] or cur in boxes[ind]:
                        return False

                    rows[r].add(cur)
                    cols[c].add(cur)
                    boxes[ind].add(cur)

        return True