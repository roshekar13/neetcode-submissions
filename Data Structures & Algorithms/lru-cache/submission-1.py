class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.tail = Node(-1,-1) # dummy values
        self.head = Node(-1,-1) # dummy values
        self.tail.next = self.head
        self.head.prev = self.tail
        # cache node objects, keyed on the key field
        self.cache = {}

    def remove(self, node):
        back = node.prev
        front = node.next
        back.next = front
        front.prev = back
        # remove dangling pointers
        node.next = None
        node.prev = None

    def add(self, node):
        curr = self.head.prev
        curr.next = node
        node.prev = curr
        node.next = self.head
        self.head.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if self.cap == self.size:
                lru = self.tail.next
                self.remove(lru)
                self.size -= 1
                del self.cache[lru.key]
            node = Node(key,value)
            self.add(node)
            self.cache[key] = node
            self.size += 1

        
