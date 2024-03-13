# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque([(p, q),])
        
        while stack:
            pC, qC = stack.pop()
            if (not pC and qC) or (pC and not qC) or (pC and qC and pC.val != qC.val):
                return False
            
            if pC:
                stack.append((pC.left, qC.left))
                stack.append((pC.right, qC.right))
        return True
            