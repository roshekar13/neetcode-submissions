from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]
        # find parent of group
        def find(curr):
            p = parent[curr]
            if p != parent[p]: return find(p)
            else: return p
        #
        def union(idx1,idx2):
            if idx1 == idx2: return # by defn
            p1,p2 = find(idx1),find(idx2)
            if p1 == p2: return # same group
            # union groups by rank
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return
        
        currAns = [0,0]
        for e1,e2 in edges:
            # arb make 1 parent if not alr present
            if find(e1) == find(e2):
                return [e1, e2]
            if find(e1) != find(e2):
                union(find(e1), find(e2))

        return currAns

        



