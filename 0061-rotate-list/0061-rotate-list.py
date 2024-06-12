# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        last = head
        
        n = 1
        while last.next:
            last = last.next
            n += 1
            
        k %= n
        
        if k == 0:
            return head
            
        idx = 1
        itr = head
        while idx < n - k:
            itr = itr.next
            idx += 1
        
        res = itr.next
        itr.next = None
        last.next = head
        
        return res