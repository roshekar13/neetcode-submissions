import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:
                if len(stack) <= 1:
                    return -1
                else:
                    y = stack.pop()
                    x = stack.pop()
                if token == '+':
                    stack.append(x+y)
                elif token == '-':
                    stack.append(x-y)
                elif token == '*':
                    stack.append(x*y)
                else:
                    if y == 0:
                        return -1
                    else:
                        stack.append(math.trunc(x/y))
            else:
                stack.append(int(token))
            print(stack)
        
        return stack.pop()
                    
                    
                
            