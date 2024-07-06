# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        counter = 0
        itr = head
        while counter < k and itr:
            itr = itr.next
            counter += 1

        if counter < k:
            return head

        prev = None
        tail = head
        itr = head
        counter = 0
        while counter < k:
            nex = itr.next
            itr.next = prev

            prev = itr
            itr = nex

            counter += 1
        
        tail.next = self.reverseKGroup(nex, k)
        
        return prev