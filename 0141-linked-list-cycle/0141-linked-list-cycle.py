# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None or head.next == None:
            return False
    
        pointer1 = head
        pointer2 = head.next.next
        
        while pointer1 != pointer2:
            if pointer1 != None:
                pointer1 = pointer1.next
            if pointer2 != None:
                pointer2 = pointer2.next
            if pointer2 != None:
                pointer2 = pointer2.next
            
            
        if pointer1 == None or pointer2 == None:
            return False
        else:
            return True