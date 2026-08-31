class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])

        def count_area(x,y):
            if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0:
                return 0
            else:
                grid[x][y] = 0
                return (1 +
                count_area(x+1,y)+
                count_area(x,y+1)+
                count_area(x-1,y)+
                count_area(x,y-1))
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    curr = count_area(i,j)
                    if curr > res: res = curr

        return res