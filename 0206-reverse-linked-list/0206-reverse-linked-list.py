# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr_1 = None
        
        while head != None:
            ptr_2 = head.next
            head.next = ptr_1
            ptr_1 = head
            head = ptr_2
            
        head = ptr_1
        return head