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
        
        if not head:
            return head
        
        dp = []
        temp = head
        while temp:
            dp.append(temp)
            temp = temp.next
        
        for i in range(len(dp) - 2, -1, -1):
            # print(i)
            dp[i + 1].next = dp[i]
        
        head.next = None
        return dp[-1]