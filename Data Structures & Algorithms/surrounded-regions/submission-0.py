class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board: return []
        m,n = len(board),len(board[0])

        # Helper DFS to mark safe territories
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and board[i][j] == 'O':
                board[i][j] = '#'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i,j+1)
            else:
                return

        # Mark safe territories
        for row in range(m):
            dfs(row,0)
            dfs(row,n-1)
        for col in range(n):
            dfs(0,col)
            dfs(m-1,col)

        for r in range(m):
            for c in range(n):
                if board[r][c]=='O': board[r][c] = 'X'
        
        for r in range(m):
            for c in range(n):
                if board[r][c]=='#': board[r][c] = 'O'
        
        