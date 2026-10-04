from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        #rank = [1 for i in range(len(edges))]

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u,v): # returntype is None
            paren_u,paren_v=find(u),find(v)
            parent[paren_v] = paren_u # make u the group parent
            return
        
        # 
        for u,v in edges:
            paren_u,paren_v = find(u),find(v)
            if paren_u == paren_v: return [u,v]
            else:
                union(u,v)
        return [-1,-1]




