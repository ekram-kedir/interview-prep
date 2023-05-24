# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        curr = head
        odd = []
        even = []
        while curr != None:
            if count % 2 == 0:
                even.append(curr.val)
            else:
                odd.append(curr.val)
            curr = curr.next
            count += 1
        result = (even + odd)
        if not result:
            return head
        value = ListNode(result[0])
        head = value
        for i in range(1,len(result)):
            newNode = ListNode(result[i])
            head.next = newNode
            head = newNode
        return value