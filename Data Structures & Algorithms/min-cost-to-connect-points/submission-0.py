import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist_matrix = dict()
        for p1,p2 in points:
            dist_matrix[(p1,p2)] = [] # heap
            for p3,p4 in points:
                if p1 == p3 and p2 == p4: continue
                dist = abs(p3-p1) + abs(p4-p2)
                heapq.heappush(dist_matrix[(p1,p2)],(dist,p3,p4)) # push new distance onto heap
        
        # starting point doenst matter- solution guarantees globally accurate solution
        total = 0
        x,y = points[0]
        seen = set()

        q = [(0,x,y)]
        # intuition: only append closest unseen point onto queue, covers each point accordingly
        while q:
            dist,x,y = heapq.heappop(q) #gets greedily optimal nearest point
            if (x,y) in seen: continue
            seen.add((x,y))
            total += dist
            for dist,x_new,y_new in dist_matrix[(x,y)]:
                if (x_new,y_new) in seen: continue
                else: heapq.heappush(q,(dist,x_new,y_new))

        return total


            