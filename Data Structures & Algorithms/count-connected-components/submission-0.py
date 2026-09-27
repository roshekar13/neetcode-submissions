class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = dict()
        for u,v in edges:
            if u not in adj_list: adj_list[u] = []
            if v not in adj_list: adj_list[v] = []
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = set()
        def explore(curr):
            seen.add(curr)
            if curr in adj_list:
                for neigh in adj_list[curr]:
                    if neigh not in seen: explore(neigh)

        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                explore(i)
        return res
            