# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        def maxcounter(tree, count):
            if tree == None:
                return count
            if tree.left == None and tree.right == None:
                return count
            else:
                return max(maxcounter(tree.left,count+1),maxcounter(tree.right,count+1))
            
        rex = maxcounter(root,1)
        return rex