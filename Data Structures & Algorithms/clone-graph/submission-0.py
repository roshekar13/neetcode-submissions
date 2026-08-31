"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        #if node.val == 0 or node.neighbors == []: return []

        clone_dict = {node: Node(node.val,[])}

        queue = [node]

        while queue:
            curr = queue.pop(0)
            for neigh in curr.neighbors:
                if neigh not in clone_dict:
                    clone_dict[neigh] = Node(neigh.val,[])
                    queue.append(neigh)
                clone_dict[curr].neighbors.append(clone_dict[neigh])
        
        return clone_dict[node]

