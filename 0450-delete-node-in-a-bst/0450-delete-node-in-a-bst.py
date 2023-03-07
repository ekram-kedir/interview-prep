# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValue(self,val):
        take = val
        while take.right:
            take = take.right
        return take
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left , key)
        elif key > root.val:
            root.right = self.deleteNode(root.right , key)
            
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                delete = self.minValue(root.left)
                
                root.val = delete.val
             
                root.left = self.deleteNode(root.left,delete.val)
        return root
                
                
            