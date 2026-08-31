# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def calclen(tree):
            if tree == None:
                return 0 #Reached a leaf
            left = calclen(tree.left) #DFS on both sides
            right = calclen(tree.right)

            self.res = max(self.res,left+right) #Updating global var
            return 1+ max(left,right) #recursive return of len
        calclen(root)
        return self.res