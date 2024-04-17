# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = None
        
        def helper(root, depth, cur):
            if not root:
                return
            
            # n = len(self.res) if self.res else float('inf')
            # if depth > n:
            #     return
            
            cur = chr(ord('a') + root.val) + cur
            if not root.left and not root.right:
                if not self.res:
                    self.res = cur
                else:
                    self.res = min(self.res, cur)
                return
                            
            helper(root.left, depth + 1, cur)
            helper(root.right, depth + 1, cur)
            
        
        helper(root, 1, "")
        return self.res
        
            