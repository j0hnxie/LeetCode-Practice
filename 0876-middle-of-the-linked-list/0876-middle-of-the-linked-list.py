# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        totalLen = 0
        temp = head
        while temp:
            temp = temp.next
            totalLen += 1
            
            
        # print(totalLen / 2 + 1)
        for i in range(totalLen / 2):
            head = head.next
        
        return head