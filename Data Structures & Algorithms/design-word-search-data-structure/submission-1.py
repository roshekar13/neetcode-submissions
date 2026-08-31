class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children: curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.is_end = True

    def search(self, word: str) -> bool:
        # handles '.' cases
        def dfs(idx, curr):
            for i in range(idx, len(word)):
                letter = word[i]

                if letter == ".":
                    # try every existing child branch
                    for child in curr.children.values():
                        if dfs(i + 1, child): return True
                    return False
                    # normal word search
                if letter not in curr.children: return False
                curr = curr.children[letter]
            
            return curr.is_end

        return dfs(0, self.root)
