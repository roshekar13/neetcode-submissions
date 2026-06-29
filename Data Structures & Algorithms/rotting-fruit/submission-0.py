class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return

        m,n = len(grid), len(grid[0])

        queue = [] #Should only contain rotten fruits
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # Search for minute 0 rotten fruits; starting points for BFS search
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    # Track number of fresh fruits
                    count += 1
        
        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        res = 0

        while queue:
            row,col,curr = queue.pop(0)

            for x,y in dirs:
                newr, newc = row+x, col+y
                if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] == 1:
                    grid[newr][newc] = 2
                    count -= 1 #Reduce fresh fruit count
                    res = max(res,curr+1) # update timestamp
                    queue.append((newr,newc,curr+1))
                    
            
        if count != 0: return -1
        else: return res
