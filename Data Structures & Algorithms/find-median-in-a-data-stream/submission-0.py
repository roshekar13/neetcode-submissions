import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # arb push to maxHeap
        heapq.heappush(self.maxHeap,-num)
        # shuffle lowest to minHeap
        heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        # check if delta > 2
        if len(self.minHeap) > len(self.maxHeap): heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self) -> float:
        # median called on empty
        if len(self.maxHeap) == len(self.minHeap) and len(self.maxHeap) == 0: return -1
        # equal length: calculate from both
        if len(self.maxHeap) == len(self.minHeap): return float((self.minHeap[0]-self.maxHeap[0])/2)
        # return maxHeap val
        else: return float(-self.maxHeap[0])
        