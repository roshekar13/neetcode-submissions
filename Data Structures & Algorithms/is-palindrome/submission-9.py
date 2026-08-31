import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low = s.lower()

        letters = list(map(chr, range(97, 123)))
        nums = set("0123456789")
        
        flag = True
        start = 0
        end = len(s_low)-1
        while start < end and flag == True:
            while start < end and s_low[start] not in letters and s_low[start] not in nums:
                start += 1 #filtering out whitespace and non alphanum chars

            while start < end and s_low[end] not in letters and s_low[end] not in nums:
                end -= 1
            #Make lowercase

            if s_low[start] == s_low[end]:
                end -= 1
                start += 1
                continue
            else:
                flag = False
        return flag