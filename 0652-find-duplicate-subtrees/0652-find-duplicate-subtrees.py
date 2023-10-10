# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        store = collections.Counter()
        ans = []
        
        def helper(root):
            
            if root is None:
                return " "
            
            left = helper(root.left)
            right = helper(root.right)
            
            subtree = (left) + "-" + (right) + "-" + str(root.val)
            store[subtree] += 1
            
            if store[subtree] == 2:
                ans.append(root)
            return subtree
        
        helper(root)
        return ans
