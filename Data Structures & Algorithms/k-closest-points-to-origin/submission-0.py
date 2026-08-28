import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            x,y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(res,(-dist,x,y))
            if len(res) > k: heapq.heappop(res)
        output = []
        for d,x,y in res: output.append([x,y])
        return output
