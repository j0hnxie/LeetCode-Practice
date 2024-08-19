# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.res1 = []
        self.res2 = []

        def helper(cur, one):
            if not cur:
                return
            
            if not cur.left and not cur.right:
                if one:
                    self.res1.append(cur.val)
                else:
                    self.res2.append(cur.val)
            
            if cur.left:
                helper(cur.left, one)
            
            if cur.right:
                helper(cur.right, one)
        
        helper(root1, True)
        helper(root2, False)

        if len(self.res1) != len(self.res2):
            return False
        
        for leaf1, leaf2 in zip(self.res1, self.res2):
            if leaf1 != leaf2:
                return False
        
        return True