class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(arr):
            s=''.join(arr).replace('.','')
            return len(s)==len(set(s))
        def checkrow():
            for row in board:
                if not valid(row):
                    return False
            return True
        def checkcol():
            for col in zip(*board):
                if not valid(col):
                    return False
            return True
        def square():
            for r in range(0,9,3):
                for c in range(0,9,3):
                    nums=[board[r+i][c+j] for i in range(3) for j in range(3)]
                    if not valid(nums):
                        return False
            return True
        return checkrow() and checkcol() and square()
