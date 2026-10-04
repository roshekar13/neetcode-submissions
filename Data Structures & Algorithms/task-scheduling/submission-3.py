from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks: return 0
        my_dict = Counter(tasks)
        cooldown = deque() # queue, timestamp and count
        timestamp = 0
        pending = [] # max-heap
        for k,v in my_dict.items():
            heapq.heappush(pending, -v)
        print(pending)

        while cooldown or pending:
            timestamp += 1
            # check cooldown
            if pending:
                curr_count = heapq.heappop(pending) + 1
                if curr_count < 0: cooldown.append((timestamp+n,curr_count))


            # check heap
            if cooldown and cooldown[0][0] == timestamp: heapq.heappush(pending, cooldown.popleft()[1])


            
        
        return timestamp

        







