# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return -1
        vals = []
        Q = deque([root])
        while Q:
            curr = Q.popleft()
            vals.append(curr.val)
            if curr.left: Q.append(curr.left)
            if curr.right: Q.append(curr.right)
        vals.sort()
        return vals[k-1]

