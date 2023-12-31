class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            element = row[-1] * (rowIndex-i+1) // i
            row.append(element)
        return row
