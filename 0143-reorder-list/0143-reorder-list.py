# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        f = head
        s = head
        prev = s
        while f and f.next:
            f = f.next.next
            prev = s
            s = s.next
        
        prev.next = None
        prev = None
        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp
        
        zero = head
        one = prev
        while zero:
            # print(zero)
            # print(one)
            zN = zero.next
            oN = one.next
            zero.next = one
            one.next = zN if zN else one.next
            zero = zN
            one = oN
        
        return head
        