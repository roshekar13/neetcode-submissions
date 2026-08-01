# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(node,curr_depth):
            if node.left is None and node.right is None: return curr_depth
            elif node.left is None: return recurse(node.right,curr_depth+1)
            elif node.right is None: return recurse(node.left,curr_depth+1)
            else: return max(recurse(node.left,curr_depth+1),recurse(node.right,curr_depth+1))
        
        if not root: return 0
        return recurse(root,1)