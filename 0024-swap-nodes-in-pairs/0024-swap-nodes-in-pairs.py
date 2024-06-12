# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        cur = temp
        
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            
            a.next = b.next
            b.next = a
            cur.next = b
            
            cur = a
        
        return temp.next