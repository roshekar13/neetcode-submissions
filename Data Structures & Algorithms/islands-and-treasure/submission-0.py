class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m,n = len(grid), len(grid[0])
        dirs = ((1,0),(0,1),(-1,0),(0,-1))

        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            row,col = queue.pop(0)

            for (x,y) in dirs:
                newr, newc = row+x, col+y

                if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] == 2147483647:
                    grid[newr][newc] = grid[row][col] + 1
                    queue.append((newr,newc))

        