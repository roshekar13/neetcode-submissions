# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node):
            if not node: return # base case 1: null node
            if node.left is None and node.right is None: return # base case 2: leaf node

            # recursive case(s) 1: only one child
            elif node.left is None:
                node.left = node.right
                node.right = None
                recurse(node.left)
            elif node.right is None:
                node.right = node.left
                node.left = None
                recurse(node.right)
            
            # recursive case 2: both children
            else:
                temp = node.left
                node.left = node.right
                node.right = temp
                recurse(node.left)
                recurse(node.right)
        
        recurse(root)
        return root