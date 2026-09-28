from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList: return 0
        wordList = set(wordList)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        q = deque([beginWord])
        res = 0
        seen = set()
        while q:
            res += 1
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                seen.add(curr)
                k = len(curr)
                for i in range(k):
                    for letter in letters:
                        word = curr[:i] + letter + curr[i+1:]
                        if word == endWord: return res+1
                        if word == curr or word in seen: continue
                        if word in wordList:
                            q.append(word)

        return 0