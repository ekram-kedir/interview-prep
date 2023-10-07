# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []
        
        def dfs(root , path , targetSum):
            if root is None:
                return
            if root.right is None and root.left is None and sum(path) + root.val == targetSum:
                path.append(root.val)
                result.append(path)
                
            dfs(root.left , path + [root.val] , targetSum)
            dfs(root.right , path + [root.val] , targetSum)
            
        dfs(root , [] , targetSum)
        return result
                