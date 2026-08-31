class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("must be greater than 0")
        self.capacity = capacity
        self.num_ele = 0
        self.storage = [None] * capacity

    def get(self, i: int) -> int:
        return self.storage[i]

    def set(self, i: int, n: int) -> None:
        self.storage[i]=n
        return


    def pushback(self, n: int) -> None:
        if self.num_ele == self.capacity:
            self.resize()
        self.storage[self.num_ele] = n
        self.num_ele += 1
        return

    def popback(self) -> int:
        self.num_ele -= 1
        temp = self.storage[self.num_ele]
        self.storage[self.num_ele] = None
        
        return temp
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        self.storage.extend([None] * (self.capacity))
        return

    def getSize(self) -> int:
        return self.num_ele
        
    
    def getCapacity(self) -> int:
        return self.capacity
