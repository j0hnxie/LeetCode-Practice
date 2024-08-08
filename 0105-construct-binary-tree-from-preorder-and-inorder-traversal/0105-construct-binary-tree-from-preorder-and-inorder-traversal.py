# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # print(preorder[0])
        # print(preorder)
        # print(inorder)

        root = TreeNode(preorder[0])
        inorder_idx = 0
        for idx, value in enumerate(inorder):
            if value == preorder[0]:
                inorder_idx = idx
                break

        root.left = self.buildTree(preorder[1:inorder_idx + 1], inorder[:inorder_idx])
        root.right = self.buildTree(preorder[inorder_idx + 1:], inorder[inorder_idx + 1:])

        return root