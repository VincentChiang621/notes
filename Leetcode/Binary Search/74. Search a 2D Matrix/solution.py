# APPROACH 1: flatten the matrix approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time O(log(m*n)) | Space: O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r :
            m = l + ((r - l) // 2)
            element = matrix[m // COLS][m % COLS]

            if element == target:
                return True
            elif element < target:
                l = m + 1
            else:
                r = m - 1

        return False
    
# APPROACH 2: Find row, then find element
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time O(log(m*n)) | Space: O(1)
        ROWS, COLS = len(matrix), len(matrix[0])

        def findRow() -> int:
            l, r = 0, ROWS - 1

            while l <= r:
                m = l + (r - l) // 2
                m_left, m_right = matrix[m][0], matrix[m][-1]

                if target < m_left:
                    r = m - 1
                elif target > m_right:
                    l = m + 1
                else:
                    return m

            return -1

        row = findRow()
        if row == -1:
            return False
        
        l, r = 0, COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            m_element = matrix[row][m]

            if target < m_element:
                r = m - 1
            elif target > m_element:
                l = m + 1
            else: 
                return True

        return False