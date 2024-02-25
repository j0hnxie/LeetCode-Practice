# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        
        tail = head
        endIndex = 1
        
        while tail.next:
            tail = tail.next
            endIndex += 1
        
        itr = head
        prev = head
        index = 1
        while index <= endIndex:
            nextNode = itr.next
            
            if index % 2 == 0:
                prev.next = nextNode
                tail.next = itr
                tail = tail.next
            else:
                prev = itr
            
            index += 1
            itr = nextNode
        
        tail.next = None
        return head
        