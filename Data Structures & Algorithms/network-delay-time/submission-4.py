import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjacency matrix
        adj_list = dict()
        for u,v,w in times:
            if u not in adj_list: adj_list[u] = []
            adj_list[u].append((w,v))
        
        # we can use a heap to updates seen nodes
        seen = set()
        global_max_time = 0
        q = [(0,k)]
        
        while q:
            #print(q)
            travel_time,node = heapq.heappop(q)
            if node not in seen:
                seen.add(node)
                global_max_time = max(global_max_time, travel_time)
                if len(seen) == n: return global_max_time # all nodes reached
                # enque node's neighbors
                if node in adj_list: # <- handles nodes with no neighbors
                    for time,neigh in adj_list[node]: heapq.heappush(q,(time+travel_time, neigh))
            
        return -1
