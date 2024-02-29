# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        
        q.append(root)
        
        level = 0
        
        while q:
            sz = len(q)
            
            prev = float('inf') if level % 2 else -1
            
            for i in range(sz):
                cur = q.popleft()
                
                if cur.val % 2 == level % 2:
                    return False
                
                if level % 2 and cur.val >= prev:
                    return False
                
                if not level % 2 and cur.val <= prev:
                    return False
                
                prev = cur.val
                
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
                    
            level += 1
        return True