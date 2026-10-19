# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1,node2):
            # base checks
            if not node1 and not node2: return 0
            if not node1 or not node2: return -1
            if node1.val != node2.val: return -1

            # recurse down
            left,right = dfs(node1.left,node2.left),dfs(node1.right,node2.right)
            if left == -1 or right == -1: return -1
            return 0
        
        return False if dfs(p,q) == -1 else True
