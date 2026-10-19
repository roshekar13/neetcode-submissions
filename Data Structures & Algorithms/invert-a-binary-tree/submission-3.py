# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            if not node: return
            if not node.left and not node.right: return # leaf or nonetype

            elif not node.left: # only right child
                temp = node.right
                node.right = None
                node.left = temp
                reverse(node.left)
            
            elif not node.right: # only left child
                temp = node.left
                node.left = None
                node.right = temp
                reverse(node.right)
            else:
                temp1,temp2 = node.left,node.right
                node.left,node.right = temp2,temp1
                reverse(node.left)
                reverse(node.right)
            
        reverse(root)
        return root