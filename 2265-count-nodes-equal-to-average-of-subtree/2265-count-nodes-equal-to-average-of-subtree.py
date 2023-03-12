# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        self.helper(root)
        
        return self.count
        
    def helper(self, root):
        if not root:
            return 0 , 0
        
        leftcall , leftcount = self.helper(root.left)
        rightcall , rightcount = self.helper(root.right)
        
        total = root.val + leftcall + rightcall
        length = leftcount + rightcount + 1
        
        if length != 0 and total // length == root.val:
            self.count += 1
        
        return total , length