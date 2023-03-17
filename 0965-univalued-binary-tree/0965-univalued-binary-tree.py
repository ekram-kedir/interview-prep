# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self , root):
        
        if not root:
            return []
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        return left + [root.val] + right
    
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        result = self.traverse(root)
        
        if len(set(result)) == 1:
            return True
        return False
        
        