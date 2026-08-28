import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        if len(stones) == 1: return stones[0]
        # min-heap --> max-heap by multiplying weights by -1
        for i in range(len(stones)): stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) > 1:
            top = heapq.heappop(stones)
            top2 = heapq.heappop(stones)
            if top == top2: continue
            else: heapq.heappush(stones,-1*(abs(abs(top2)-abs(top))))
        if not stones: return 0
        else: return -1*stones[0]