"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.height = 0
        
        def dfs(curr_node,level):
            
            if curr_node is None:
                return 
            
            self.height = max(level , self.height)
            
            for node in curr_node.children:
                    dfs(node,level+1)
                    
        dfs(root , 1)
      
        return self.height