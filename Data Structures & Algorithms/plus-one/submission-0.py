class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        rev_dig = digits[::-1]
        flag = True
        curr = 0
        while flag:
            if rev_dig[curr] == 9: #check for 9
                rev_dig[curr] = 0
                if curr == len(digits)-1: # check if need to add new digit place
                    rev_dig.append(1)
                    flag = False
            else:
                rev_dig[curr] += 1
                flag = False
            curr += 1
        
        return rev_dig[::-1]
