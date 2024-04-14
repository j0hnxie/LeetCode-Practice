# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def helper(root, leftChild):
            if not root:
                return
            
            if not root.left and not root.right and leftChild:
                self.total += root.val
            
            helper(root.left, True)
            helper(root.right, False)
        
        helper(root, False)
        return self.total