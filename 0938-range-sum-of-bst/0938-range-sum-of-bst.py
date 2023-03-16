# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        
        if not root:
            return []
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        return left + [root.val] + right
        
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        total = 0
        result = self.traverse(root)
        
        for num in result:
            
            if num >= low and num <= high:
                total += num
        return total
   