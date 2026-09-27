class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = dict()
        if n == 1: return True
        if not edges or len(edges) != n-1: return False
        
        for u,v in edges:
            if u not in adj_list: adj_list[u] = []
            if v not in adj_list: adj_list[v] = []
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        seen = set()
        processed = set()
        def dfs(curr,par):
            seen.add(curr)
            if curr in adj_list:
                for neigh in adj_list[curr]:
                    if neigh in processed: continue
                    if neigh == par: continue
                    if neigh in seen: return False
                    if not(dfs(neigh,curr)): return False
            else: return False
            #seen.remove(curr)
            processed.add(curr)
            return True
        
        return len(seen) == n if dfs(0,-1) else False
            