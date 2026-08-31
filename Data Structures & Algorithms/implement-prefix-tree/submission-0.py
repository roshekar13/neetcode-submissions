class Node:
    def __init__(self):
        self.child = {}
        self.EOW = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.child:
                curr.child[i] = Node()
            curr = curr.child[i]
        curr.EOW = True
        return

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return curr.EOW

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i not in curr.child:
               return False
            curr = curr.child[i]
        return True 
        