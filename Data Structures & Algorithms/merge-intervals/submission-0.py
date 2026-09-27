class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        if not intervals: return 0
        res = []
        for st,end in intervals:
            if not res:
                res.append((st,end))
                continue
            curr_st,curr_end = res[-1]
            if curr_end >= st:
                curr_st,curr_end = res.pop()
                res.append((min(st,curr_st),max(end,curr_end)))
            else:
                res.append((st,end))

        
        return res

            
