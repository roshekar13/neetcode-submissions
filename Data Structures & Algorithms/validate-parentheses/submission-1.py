class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', '}':'{',']':'['}
        for i in s:
            if i in dic:
                if stack and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    print('fucakss')
                    print(i)
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False