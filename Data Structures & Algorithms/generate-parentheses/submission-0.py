class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def build(curr,open_count,close_count):
            if len(curr) == n*2:
                res.append(curr)
                return
            if open_count < n: build(curr+'(',open_count+1,close_count)
            if close_count < open_count: build(curr+')',open_count,close_count+1)
        build('',0,0)
        return res
