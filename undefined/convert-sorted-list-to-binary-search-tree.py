# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def recur(node):
            if node == None:
                return None
            if node.next == None:   return TreeNode(node.val)
            slow = fast = node
            prevDum = ListNode(0, slow)
            while fast != None and fast.next != None:
                slow = slow.next
                prevDum = prevDum.next
                fast = fast.next.next
            prevDum.next = None
            root = TreeNode(slow.val)
            root.left = recur(node)
            root.right = recur(slow.next)
            return root
        return recur(head)