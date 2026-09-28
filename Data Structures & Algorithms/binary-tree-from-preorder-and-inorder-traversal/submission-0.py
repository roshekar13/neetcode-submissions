# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            # Base case: if there are no elements to construct this subtree
            if left > right:return None
            
            # The current root value is at the current preorder index
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Find the root's index in the inorder array
            mid = inorder_idx[root_val]
            
            # Recursively build the left and right subtrees
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            
            return root
            
        return dfs(0, len(inorder) - 1)
        