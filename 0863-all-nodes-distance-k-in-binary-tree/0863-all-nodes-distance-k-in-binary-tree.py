# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root , parent):
    
        if root:
            self.parents[root.val] = parent
            self.dfs(root.left , root)
            self.dfs(root.right , root)
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
            self.parents = defaultdict(int)
            self.dfs(root,None)
            
            visited = set([(target)])
            queue = [target]
            level = 0
            
            if k == 0:
                return [target.val]
            
            while queue:

                if level == k:
                    return [node.val for node in queue]
                
                level += 1
                length = len(queue)

                for ele in range(length):
                    node = queue.pop(0)
                    
                    if self.parents[node.val] not in visited and self.parents[node.val] is not None:
                        visited.add(self.parents[node.val])
                        queue.append(self.parents[node.val])
                    if node.left and node.left not in visited:
                        visited.add(node.left)
                        queue.append(node.left)
                    if node.right and node.right not in visited:
                        visited.add(node.right)
                        queue.append(node.right)
            
                        
               
            return []
    