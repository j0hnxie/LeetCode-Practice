# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l2H = list2
        l2T = list2
        
        counter = 0
        
        while l2T.next:
            l2T = l2T.next
        
        l1H = list1
        l1T = list1
        
        prev = None
        while counter < a - 1:
            l1T = l1T.next
            counter += 1
            
        skip = l1T.next
        l1T.next = l2H
        l1T = skip
        counter += 1
        
        while counter < b:
            l1T = l1T.next
            counter += 1
        
        l2T.next = l1T.next
        
        return l1H