# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        cur = []

        while fast and fast.next:
            cur.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        idx = 0
        n = len(cur)
        while slow:
            cur[n - 1 - idx] += slow.val
            slow = slow.next
            idx += 1
        
        return max(cur)