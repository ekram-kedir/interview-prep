# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        visited = set([root])
        queue = deque([root])
        answer = []
        
        while queue:
            total = 0
            length = len(queue)
      
            for ele in range(length):
                node = queue.popleft()
                total += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                
            answer.append(total/length)
            total = 0
        
        return answer