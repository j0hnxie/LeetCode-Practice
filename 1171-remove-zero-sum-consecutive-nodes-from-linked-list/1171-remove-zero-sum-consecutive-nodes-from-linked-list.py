# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        ans = head
        itr = head
        pre = 0
        found = {0: dummy}
        
        while itr:
            pre += itr.val
            if pre in found:
                keep_node = found[pre]
                cur = keep_node.next
                
                temp_pre = pre + cur.val
                while cur != itr:
                    del found[temp_pre]
                    cur = cur.next
                    temp_pre += cur.val
                
                keep_node.next = itr.next
            else:
                found[pre] = itr
            itr = itr.next
        return dummy.next