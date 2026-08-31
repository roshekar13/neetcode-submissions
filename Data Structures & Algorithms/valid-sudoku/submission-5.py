class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row + Colcheck
        n = len(board)
        for r in range(n):
            r_set = set()
            c_set = set()
            for c in range(n):
                if board[r][c] in r_set:
                    return False
                elif board[r][c] not in r_set and board[r][c] != ".":
                    r_set.add(board[r][c])
                
                if board[c][r] in c_set:
                    return False
                elif board[c][r] not in c_set and board[c][r] != ".":
                    c_set.add(board[c][r])
                
        #reached here, row + col check done

        #Box check
        quads = [[0,1,2],[3,4,5],[6,7,8]]
        for i in quads:
            for j in quads:
                q_set = set()
                for i_int in i:
                    for j_int in j:
                        if board[i_int][j_int] in q_set:
                            return False
                        elif board[i_int][j_int] not in q_set and board[i_int][j_int] != ".":
                            q_set.add(board[i_int][j_int])
                        
        return True
        


