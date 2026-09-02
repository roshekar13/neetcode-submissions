import heapq
# intuition: preserve only k largest numbers, heappop during add() to get lowest
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        self.k = k
        heapq.heapify(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        return heapq.nlargest(self.k, self.q)[self.k-1]
        
