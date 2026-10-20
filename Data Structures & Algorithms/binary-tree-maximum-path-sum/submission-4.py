# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float('-inf')
        def dfs(node):
            if not node: return 0
            
            lsum,rsum = max(0,dfs(node.left)),max(0,dfs(node.right))

            self.maxPathSum = max(self.maxPathSum, lsum+rsum+node.val)
            return max(lsum,rsum)+node.val
        
        dfs(root)
        return self.maxPathSum
        