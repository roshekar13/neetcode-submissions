class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        w_len = len(word)
        m,n = len(board),len(board[0])
        
        def backtrack(i,j,idx):

            if idx == w_len: return True
            if i<0 or j<0 or i>=m or j>=n or board[i][j]!= word[idx]: return False

            temp = board[i][j]
            board[i][j] = '0'
            
            found = backtrack(i+1,j,idx+1) or backtrack(i-1,j,idx+1) or backtrack(i,j+1,idx+1) or backtrack(i,j-1,idx+1)
            board[i][j] = temp

            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0): return True
        
        return False





