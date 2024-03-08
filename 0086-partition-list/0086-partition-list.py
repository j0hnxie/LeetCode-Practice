# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead = ListNode(val=-1000)
        lessTail = lessHead
        greatHead = ListNode(val=-1000)
        greatTail = greatHead
        
        while head:
            # print(head)
            if head.val < x:
                lessTail.next = head
                lessTail = head
            else:
                greatTail.next = head
                greatTail = head
            head = head.next
        
        lessTail.next = greatHead.next
        greatTail.next = None
        return lessHead.next
        