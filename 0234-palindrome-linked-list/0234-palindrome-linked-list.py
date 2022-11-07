# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur=head
        l=0
        while cur:
            l+=1
            cur=cur.next
        mid=l//2
        s=0
        def helper(head):
            res=None
            while head:
                nex=head.next
                head.next=res
                res=head
                head=nex
            return res
        start = then = head
        while s<mid:
            then=then.next
            s+=1
        then = helper(then)
        while start and then:
            if start.val != then.val: return False
            start=start.next
            then=then.next
        return True 