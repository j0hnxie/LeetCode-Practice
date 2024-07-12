# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(cur):
            if not cur:
                return float('inf')
            if not cur.left and not cur.right:
                return 1

            leftDepth = helper(cur.left)
            rightDepth = helper(cur.right)
            minDepth = min(leftDepth, rightDepth) + 1
            return minDepth
        
        return helper(root)
        
            