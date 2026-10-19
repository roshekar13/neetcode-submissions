# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        count = [0]
        def dfs(node,local_max):
            if node.val >= local_max:
                local_max = node.val
                count[0]+= 1
            if node.left: dfs(node.left,local_max)
            if node.right: dfs(node.right,local_max)
            return
        dfs(root,float('-inf'))
        return count[0]
