class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        rDiag = set()
        lDiag = set()
        res = []

        def backtrack(row: int) -> List[List[str]]:
            # we need to return a copy of the board
            if row == n:
                res.append(["".join(r) for r in board])
                return
        
            for col in range(n):
                # check for attacking queen
                if (col in cols) or ((row-col) in rDiag) or ((row+col) in lDiag): continue
                # made it here: valid (r,c) candidate for Queen position

                # track blocked positions
                cols.add(col)
                rDiag.add(row-col)
                lDiag.add(row+col)
                # update board
                board[row][col] = 'Q'
                # backtrack
                backtrack(row+1)
                # undo moves to explore new paths
                cols.remove(col)
                rDiag.remove(row-col)
                lDiag.remove(row+col)
                board[row][col] = '.'
        
        backtrack(0)
        return res
            