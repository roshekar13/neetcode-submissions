# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        Q = deque([root])
        while Q:
            l = len(Q)
            for i in range(l):
                curr = Q.popleft()
                if curr.left is not None: Q.append(curr.left)
                if curr.right is not None: Q.append(curr.right)
                if i == l-1: res.append(curr.val)
            
        return res


