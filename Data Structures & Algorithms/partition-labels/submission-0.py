from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        my_dict = Counter(s)
        res = []
        seen = set()
        curr = 0
        for i in s:
            print(i)
            
            # new item: add to seen set and decrement hash
            if i not in seen:
                print('this')
                my_dict[i] -= 1
                seen.add(i)
                curr += 1
                print(seen,'\n')
            # recurring item: decrement hash
            else:
                print('updating')
                my_dict[i] -= 1
                curr += 1

            # remove from i from seen set if all instances exhausted
            if my_dict[i] == 0:
                print('thiss',seen,i)
                seen.remove(i)
                print('that',seen)

            # exit condition: nothing on queue
            if not seen:
                print('oops')
                res.append(curr)
                curr = 0
        
        return res

            

        