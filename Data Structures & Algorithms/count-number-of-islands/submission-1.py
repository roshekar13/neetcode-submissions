class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define a helper function to mark off an island
        if not grid: return 0
        m,n = len(grid),len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def sink_island(r,c):
            if not(0<=r<m and 0<=c<n) or grid[r][c] == '0': return
            # sink
            grid[r][c] = '0'
            for dr,dc in dirs:
                sink_island(dr+r,dc+c)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    sink_island(i,j)
        return res