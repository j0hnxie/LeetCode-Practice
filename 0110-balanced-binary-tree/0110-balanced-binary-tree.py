# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def heightFind(self, root):
            if not root:
                return 0, True
            
            leftHeight, leftTF = heightFind(self, root.left)
            rightHeight, rightTF = heightFind(self, root.right)
            height = max(leftHeight, rightHeight) + 1
            tf = (leftTF and rightTF)
            if abs(leftHeight - rightHeight) > 1:
                tf = False
            
            # print(str(root.val) + " " + str(tf) + " " + str(leftHeight) + " " + str(rightHeight))
            return height, tf
        
        heightResult, tfResult = heightFind(self, root)
        return tfResult
        