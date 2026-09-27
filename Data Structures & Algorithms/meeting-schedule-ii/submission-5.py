"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key = lambda x: x.start)
        res = 0
        heap = []
        for inter in intervals:
            #if not heap: heapq.heappush(heap, inter.end)
            #print(heap[0],inter.start,inter.end)
            if heap and heap[0] <= inter.start:
                heapq.heappop(heap)
                heapq.heappush(heap, inter.end)
            else:
                heapq.heappush(heap, inter.end)
        print(heap)
        return len(heap)