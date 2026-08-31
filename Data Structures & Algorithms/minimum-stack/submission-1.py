class MinStack:

    def __init__(self):
        self.values = []
        self.sTop = None
        self.minval = []

    def push(self, val: int) -> None:
        self.values.append(val)
        self.sTop = val
        if self.minval == []:
            self.minval.append(val)
        elif self.minval[-1] >= val:
            self.minval.append(val)
        

    def pop(self) -> None:
        val = self.values.pop()
        if self.values == []:
            self.sTop = None
        else:
            self.sTop = self.values[-1]
        if val == self.minval[-1]:
            self.minval.pop()

    def top(self) -> int:
        return self.sTop

    def getMin(self) -> int:
        return self.minval[-1]
        
