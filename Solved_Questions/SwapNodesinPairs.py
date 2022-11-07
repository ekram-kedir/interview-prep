# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# ANSWER

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new=ListNode(0,head)
        p,p1=new,head
        while p1 and p1.next:
            nxtround=p1.next.next
            second=p1.next
            second.next=p1
            p1.next=nxtround
            p.next=second
            p=p1
            p1=nxtround
        return new.next
