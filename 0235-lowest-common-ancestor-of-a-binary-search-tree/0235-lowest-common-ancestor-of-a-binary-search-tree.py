# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        res = None
        
        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                return root
            
        return -1