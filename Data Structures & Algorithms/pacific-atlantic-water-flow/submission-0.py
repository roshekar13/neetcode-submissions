class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # Initialize problem set
        if not heights: return []
        m,n = len(heights), len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # Initialize boolean grids
        atl = [[False for _ in range (n)] for _ in range (m)]
        pac = [[False for _ in range (n)] for _ in range (m)]
        res = []
        
        # generic helper DFS
        def dfs(i,j,curr):
            # Mark reachable
            curr[i][j] = True

            for x,y in dirs:
                newr, newc = i+x, j+y
                if 0 <= newr < m and 0 <= newc < n and not curr[newr][newc]:
                    if heights[i][j] <= heights[newr][newc]:
                        dfs(newr,newc,curr)
        
        for rows in range (m):
            dfs(rows,0,pac)
            dfs(rows,n-1,atl)

        for cols in range (n):
            dfs(0,cols,pac)
            dfs(m-1,cols,atl)


        # Filter valid coordinates
        for i in range(m):
            for j in range(n):
                if atl[i][j] and pac[i][j]: res.append([i,j])
        
        return res
            
