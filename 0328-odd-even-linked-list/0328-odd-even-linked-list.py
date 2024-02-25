# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        oddHead = head
        evenHead = head.next
        oddTail = head
        evenTail = head.next
        itr = head.next.next
        evenTail.next = None
        index = 3
        
        while itr:
            # print(itr)
            nextNode = itr.next
            if index % 2 == 0:
                evenTail.next = itr
                itr.next = None
                evenTail = evenTail.next
            else:
                oddTail.next = itr
                itr.next = None
                oddTail = oddTail.next
            
            index += 1
            itr = nextNode
        
        oddTail.next = evenHead
        return oddHead
        