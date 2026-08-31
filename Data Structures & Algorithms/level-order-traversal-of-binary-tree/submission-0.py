# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        #res.append([root.value])
        q.append(root)
        while q:
            curr = []
            curr_len = len(q)
            for i in range(curr_len):
                node = q.pop(0)
                if node: #NULL Check
                    curr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curr: #Checking that we dont add an empty level to the list
                res.append(curr)
        return res



