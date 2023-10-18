# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans1 = ""
        cur = l1
        while cur is not None:
            ans1 += str(cur.val)
            cur = cur.next
        
        ans2 = ""
        cur = l2
        while cur is not None:
            ans2 += str(cur.val)
            cur = cur.next
            
        result = int(ans1) + int(ans2)
        value = ListNode(str(result)[0])
        head = value
        
        for i in range(1,len(str(result))):
            newNode = ListNode(str(result)[i])
            head.next = newNode
            head = newNode

        return value

