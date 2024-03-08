# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def diameter(root):
            # print(root)
            if not root:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            self.diam = max(self.diam, (left - 1) + (right - 1) + 2)
            return max(left, right) + 1
        diameter(root)
        return self.diam