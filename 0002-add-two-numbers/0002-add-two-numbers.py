# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        str1, str2 = "", ""
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
            
        result = int(str1[::-1]) + int(str2[::-1])
        
        size = len(str(result))
        head = ListNode(int(str(result)[-1]))
        temp = head
        for i in range(size - 2, -1, -1):
            temp.next = ListNode(int(str(result)[i]))
            temp = temp.next
            # print(temp)
            
        temp.next = None
        return head
            