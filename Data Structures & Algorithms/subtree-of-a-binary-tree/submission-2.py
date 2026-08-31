# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Take care of base cases
        if not root and not subRoot:
            return True
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        #Comparison function
        def cmp_eq(tree1,tree2):
            if tree1 == None and tree2 == None:
                return True
            if (tree1 == None and tree2) or(tree1 and tree2 == None):
                return False
            else:
                if tree1.val != tree2.val:
                    return False
                else:
                    return cmp_eq(tree1.left,tree2.left) and cmp_eq(tree1.right,tree2.right)
        #DFS on main tree and comparing at each level
        def dfs(tree):
            if cmp_eq(tree,subRoot):
                return True
            if not tree:
                return False
            return dfs(tree.left) or dfs(tree.right)

        return dfs(root) or cmp_eq(root,subRoot)