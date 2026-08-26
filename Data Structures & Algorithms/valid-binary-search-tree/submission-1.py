# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root: return True
        Q = deque([(root,float('-inf'),float('inf'))])

        while Q:
            curr, lb, ub = Q.popleft()
            if not(lb < curr.val < ub): return False
            if curr.left: Q.append((curr.left, lb, curr.val))
            if curr.right: Q.append((curr.right, curr.val, ub))

        return True