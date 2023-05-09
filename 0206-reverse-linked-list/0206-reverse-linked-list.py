# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        stack = []
        
        if head:
            stack.append(head)
        prev = None
        while stack:
            top = stack.pop()
            
            if top.next:
                stack.append(top.next)
            
            top.next = prev
            prev = top
            
        return prev