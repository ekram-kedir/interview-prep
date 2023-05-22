# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new= ListNode()
        val = new
        res = 0
        while l1 or l2 or res:
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            
            val.next = ListNode(res%10)
            val = val.next
            res //= 10
        
        return new.next