class Solution:
    def checkValidString(self, s: str) -> bool:
        minCount = 0
        maxCount = 0

        for paren in s:
            if paren == '(':
                minCount += 1
                maxCount += 1
            elif paren == ')':
                minCount -= 1
                maxCount -= 1
            elif paren == '*':
                minCount -= 1
                maxCount += 1
        
            if maxCount < 0: return False
            minCount = max(minCount,0)

        return minCount == 0