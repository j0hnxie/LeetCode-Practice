# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        pq = []
        counter = 0
        
        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, counter, l))
                counter += 1
        
        res = ListNode()
        itr = res
        while pq:
            val, temp, cur = heapq.heappop(pq)
            itr.next = cur
            itr = itr.next
            
            if cur.next:
                heapq.heappush(pq, (cur.next.val, counter, cur.next))
                counter += 1
        
        return res.next