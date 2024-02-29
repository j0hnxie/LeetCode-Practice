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
        s = []
        
        front = head
        
        while head:
            s.append(head)
            head = head.next
        back = s.pop()
        
        while front != back and front.next != back:
            # print(front)
            # print(back)
            temp = front.next
            front.next = back
            back.next = temp
            
            front = temp
            back = s.pop()
            
#         if front == back:
#             front.next = 
        back.next = None
            
        return head