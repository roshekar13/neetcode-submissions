import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        col = set()
        lDiag = set()
        rDiag = set()
        res = []
        def backtrack(r):
            if r == n:
                # deep copy current board state
                curr = []
                for i in range(n):
                    row = ""
                    for j in range(n):
                        row += board[i][j]
                    curr.append(row)
                res.append(curr)
                return
            
            for i in range(n):
                if i not in col and r-i not in lDiag and (r+i) not in rDiag:
                    # trial new queen placement
                    board[r][i] = 'Q'
                    col.add(i)
                    rDiag.add(r+i)
                    lDiag.add(r-i)
                    
                    # recurse further
                    backtrack(r+1)

                    # undo changes
                    board[r][i] = '.'
                    rDiag.remove(r+i)
                    lDiag.remove(r-i)
                    col.remove(i)
            return

        backtrack(0)
        return res
        