class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # define variables for direction & direction changes
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        curr_dir = 0 # start facing right

        # define variables for the bounds
        m,n = len(matrix), len(matrix[0])
        left, top = -1,-1
        right, bottom = n,m

        # define variables to track position, # additions, and output
        total = 0
        r,c = 0,0
        res = []

        while total < m*n:
            print(total,m,n)
            res.append(matrix[r][c])
            total += 1
            if total == m*n: return res

            dr,dc = dirs[curr_dir]
            nr,nc = r+dr,c+dc
            if not((left < nc < right) and (top < nr < bottom)):
                # update boundaries based on curr_dir
                if curr_dir == 0: top = r
                elif curr_dir == 1: right = c
                elif curr_dir == 2: bottom = r
                elif curr_dir == 3: left = c
                # update direction
                curr_dir = (curr_dir+1)%4
                # update lookahead directions
                dr,dc = dirs[curr_dir]
                nr,nc = r+dr,c+dc
            r,c =nr,nc
        return res

