# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == []:
            return True
        
        def dfs(tree):
            if tree == None:
                return 0
            
            left = dfs(tree.left)
            right = dfs(tree.right)
            if left == -1 or right == -1:
                return -1
            
            if abs(left-right) > 1:
                return -1
            
            return max(left,right) + 1

        res = dfs(root)
        if res == -1:
            return False
        return True