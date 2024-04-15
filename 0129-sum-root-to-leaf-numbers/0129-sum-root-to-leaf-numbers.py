# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def helper(root, cur):
            if not root:
                return
            
            cur += str(root.val)
            
            if not root.left and not root.right:
                self.total += int(cur)
            
            helper(root.left, cur)
            helper(root.right, cur)
        helper(root, "")
        return self.total