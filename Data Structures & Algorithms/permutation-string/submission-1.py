class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        print(s2[0:3])
        for i in s1:
            if i not in s1_dict:
                s1_dict[i] = 1
            else:
                s1_dict[i] += 1
        s2_dict = {}
        n = len(s1)
        l = 0
        r = n
        while r <= len(s2):
            s2_dict = {}
            for i in s2[l:r]:
                if i not in s1_dict:
                    continue
                else:
                    if i not in s2_dict:
                        s2_dict[i] = 1
                    else:
                        s2_dict[i] += 1
            if s1_dict == s2_dict:
                return True
            else:
                l += 1
                r += 1
                continue
                
        return False
