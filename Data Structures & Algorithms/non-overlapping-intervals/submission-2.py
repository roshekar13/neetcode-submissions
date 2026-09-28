class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        heap = []
        res = 0
        prev = intervals[0][1]
        for i in range(1,len(intervals)):
            st,end = intervals[i]
            if st < prev: res += 1 # discard and increase
            else: prev = end
        return res
