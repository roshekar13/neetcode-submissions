class Node:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        
        trie = Node()
        for word in words:
            curr = trie
            for letter in word:
                if letter not in curr.children: curr.children[letter] = Node()
                curr = curr.children[letter]
            curr.isEnd = True
        
        m,n = len(board),len(board[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        res = []


        def dfs(x,y,curr,curr_word,curr_path):
            # OOB / path check
            if x < 0 or y < 0 or x >= m or y >= n: return
            if (x,y) in curr_path: return

            # check if no more children in trie
            letter = board[x][y]
            if letter not in curr.children: return

            # append if
            curr_word += letter
            curr = curr.children[letter]
            if curr.isEnd:
                res.append(curr_word)
                curr.isEnd = False # dedupe
            
            curr_path.add((x,y))

            # not- traverse all 4 directions
            for dx,dy in dirs:
                dfs(x+dx, y+dy, curr,curr_word,curr_path)
            
            curr_path.remove((x,y))



        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie.children: dfs(r,c,trie,'',set())
        
        return res