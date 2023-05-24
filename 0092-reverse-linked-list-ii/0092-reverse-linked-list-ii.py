# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        count = 0
        curr = head
        array = []
        
        while curr != None:
            array.append(curr.val)
            curr = curr.next
            count += 1
            
        if left < len(array) and right <= len(array):
            
            index1 = left - 1
            index2 = right - 1
            while index1 < index2:
                array[index1],array[index2] = array[index2],array[index1]
                index1 += 1
                index2 -= 1
                
        if not array:
            return head
        
        value = ListNode(array[0])
        head = value
        for i in range(1,len(array)):
            newNode = ListNode(array[i])
            head.next = newNode
            head = newNode
        return value
          