# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
      
    def helper(self ,node , cur, targetSum):
                if not node:  
                    return
                self.helper(node.left , cur + node.val, targetSum)
                self.helper(node.right , cur + node.val, targetSum)
                if cur + node.val == targetSum:
                    self.count += 1
    def dfs(self ,node, targetSum):
                if not node:
                    return
                self.helper(node , 0, targetSum)
                self.dfs(node.left, targetSum)
                self.dfs(node.right,targetSum)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
            self.count = 0
            self.dfs(root, targetSum)
            return self.count