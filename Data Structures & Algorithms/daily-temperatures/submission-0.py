class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        curr_idx = 0
        
        n = len(temperatures)

        while curr_idx < n:
            counter = 0
            flag = False
            curr = temperatures[curr_idx]

            for i in range(curr_idx,n):
                if temperatures[i] > curr:
                    flag = True
                    break # Have encountered a higher temp
                else: counter += 1 # Continue searching
            
            if flag: res.append(counter)
            else: res.append(0)
            curr_idx += 1
        
        return res