# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.take = defaultdict(list)
        self.helper(root , 0 , 0)
        
        answer = []
        print(self.take)
        
        
        for key in sorted(self.take.keys()):
            
            answer.append(self.take[key][-1][1])
        
        return answer
    def helper(self, root , row, col):
        if not root:
            return

        self.take[row].append((col,root.val))

        self.helper(root.left , row + 1, col - 1)
        self.helper(root.right ,row + 1 , col + 1)

        
        