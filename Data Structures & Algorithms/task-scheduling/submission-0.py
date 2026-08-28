from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        cooldown_q = deque() # cooldown tracker
        task_counts = [-x for x in hashmap.values()] # task counter
        heapq.heapify(task_counts)

        timestamp = 0
        while cooldown_q or task_counts:
            timestamp += 1
            if cooldown_q: # check if latest task on cooldown can be added back to heap
                curr = cooldown_q[0]
                if curr[1]+1 == timestamp:
                    heapq.heappush(task_counts, curr[0])
                    cooldown_q.popleft()
            if task_counts: # cpu can run task right now
                curr = heapq.heappop(task_counts)
                curr += 1 # do one task
                if curr<0: cooldown_q.append((curr,timestamp+n))# add to cooldown queue
            
        return timestamp
            
