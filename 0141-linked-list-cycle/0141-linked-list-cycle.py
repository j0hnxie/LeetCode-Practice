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
        
        def cycleHelper(self, head, visited):
            # print(head.val)
            if not head:
                return False
            elif head in visited:
                return True
            
            visited.add(head)
            return cycleHelper(self, head.next, visited)
        
        visit = set()
        return cycleHelper(self, head, visit)
            