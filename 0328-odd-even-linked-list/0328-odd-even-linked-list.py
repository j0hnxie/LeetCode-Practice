# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx = 1
        even_head = ListNode()
        even_tail = even_head
        odd_head = ListNode()
        odd_tail = odd_head


        while head:
            nex = head.next

            if idx % 2:
                odd_tail.next = head
                odd_tail = head
            else:
                even_tail.next = head
                even_tail = head
            head.next = None

            head = nex
            idx += 1
        
        odd_tail.next = even_head.next
        return odd_head.next