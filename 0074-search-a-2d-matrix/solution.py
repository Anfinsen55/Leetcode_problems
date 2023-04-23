class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        i, j = 0, (rows * columns) - 1

        while i <= j:
            mid = (i+j) >> 1
            mid_elements = matrix[mid // columns][mid % columns]
            if mid_elements == target:
                return True
            elif mid_elements < target:
                i = mid + 1
            else:
                j=mid -1
        return False
