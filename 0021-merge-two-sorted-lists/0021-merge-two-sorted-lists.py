# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        # head = list1
        # cur = head
        # cur1 = list1.next
        # cur2 = list2
        if list1.val < list2.val:
            head = list1
            cur = head
            cur1 = list1.next
            cur2 = list2
        else:
            head = list2
            cur = head
            cur1 = list1
            cur2 = list2.next
        
#         print(cur1.val)
#         print(cur2.val)
            
        while cur1 != None and cur2 != None:
            if (cur1.val < cur2.val):
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            # print(cur.val)
            cur = cur.next
        
        if cur1 != None:
            cur.next = cur1
        else:
            cur.next = cur2
        
        return head
            

            
        
            