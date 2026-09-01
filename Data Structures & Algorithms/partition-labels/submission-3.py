from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        my_dict = Counter(s)
        res = []
        seen = set()
        curr = 0
        for i in s:
            # new item: add to seen set and decrement hash
            if i not in seen:
                my_dict[i] -= 1
                seen.add(i)
                curr += 1
            
            # recurring item: decrement hash
            else:
                my_dict[i] -= 1
                curr += 1

            # remove from i from seen set if all instances exhausted
            if my_dict[i] == 0: seen.remove(i)

            # exit condition: nothing on queue
            if not seen:
                res.append(curr)
                curr = 0
        
        return res

            

        