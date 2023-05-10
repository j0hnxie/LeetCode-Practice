# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # result = 0
        
        def helper(root):
            if not root:
                return 0
            
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            if (leftHeight + rightHeight) > self.result:
                self.result = leftHeight + rightHeight
            
            return max(leftHeight, rightHeight) + 1
        
        helper(root)
        
        return self.result
        