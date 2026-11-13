class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        l = 0
        r = (ROWS * COLUMNS ) - 1

        while l <= r:
            mid = (l+r) // 2
            row = mid // COLUMNS
            col = mid % COLUMNS

            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] == target:
                return True

        return False