# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        offset = head
        counter = 0
        while counter < n:
            offset = offset.next
            counter += 1
        
        prev = None
        cur = head
        while offset:
            offset = offset.next
            prev = cur
            cur = cur.next
            
        
        if not prev:
            return head.next
        else:
            prev.next = cur.next
            return head
        
        