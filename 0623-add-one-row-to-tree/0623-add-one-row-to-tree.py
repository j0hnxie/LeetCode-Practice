# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            new_root = TreeNode(val=val, left=root, right=None)
            return new_root
        
        
        def add(r, v, d):
            if not r:
                return
            
            if d == depth - 1:
                new_left = TreeNode(val=val, left=r.left, right=None)
                new_right = TreeNode(val=val, left=None, right=r.right)
                r.left = new_left
                r.right = new_right
                
            add(r.left, v, d + 1)
            add(r.right, v, d + 1)
        
        add(root, val, 1)
        return root