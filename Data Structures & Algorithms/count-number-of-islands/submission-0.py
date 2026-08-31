class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define a helper function to mark off an island
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])
        def sink_island(x,y):
            if x >= n or x < 0 or y < 0 or y >= m or grid[x][y] =='0':
                return
            else:
                grid[x][y] = '0'
                sink_island(x+1,y)
                sink_island(x,y+1)
                sink_island(x-1,y)
                sink_island(x,y-1)
                return

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    sink_island(i,j)
        
        return res