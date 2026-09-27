import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if not flights: return -1
        adj_list = dict()
        for fr,to,pr in flights: # from, to, price
            if fr not in adj_list: adj_list[fr] = []
            adj_list[fr].append((pr,to)) # index price first, will be useful for min-heap of cheapest prices
        
        min_node = dict() # <= fix: use it to tack the min number of stops per node
        q = [(0,src,0)] # we will enqueue (price, destination, num_flights)

        while q:
            curr_price,curr,curr_num = heapq.heappop(q)
            if curr in min_node and min_node[curr] <= curr_num: continue # current enqueued is less eff
            min_node[curr] = curr_num # cache the new lowest # stops to get here
            # check if we reached
            if curr == dst: return curr_price
            # search airport's neighbors
            if curr in adj_list and curr_num <= k:
                for neigh_pr,neigh in adj_list[curr]:
                    heapq.heappush(q,(curr_price+neigh_pr,neigh,curr_num+1))
        
        return -1
