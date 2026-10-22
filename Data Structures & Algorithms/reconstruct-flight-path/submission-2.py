class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        num_stops = 0
        adj_list = dict()

        for src,dst in tickets:
            if src not in adj_list: adj_list[src] = []
            adj_list[src].append(dst)
        
        for k in adj_list: adj_list[k].sort()
        
        res = []
        def dfs(curr):
            while curr in adj_list and adj_list[curr]:
                nxt = adj_list[curr].pop(0)
                dfs(nxt)
            res.append(curr)
        
        dfs('JFK')
        return res[::-1]

        