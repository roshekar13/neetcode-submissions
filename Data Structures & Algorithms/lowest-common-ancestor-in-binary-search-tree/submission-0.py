# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return -1
        ub,lb = max(p.val,q.val),min(p.val,q.val)
        def traverse(curr):
            if not curr: return None #null access safeguard
            if lb <= curr.val <= ub: return curr # check if we found LCA
            elif curr.val > ub: return traverse(curr.left) # current ancestor > UB: traverse left
            else: return traverse(curr.right) # traverse right
        
        return traverse(root)