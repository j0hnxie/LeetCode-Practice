# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        stack = deque()
        if root != None:
            stack.append(root)
        while stack:
            top = stack.pop()
            temp = top.left
            top.left = top.right
            top.right = temp
            
            if top.left != None:
                stack.append(top.left)
            if top.right != None:
                stack.append(top.right)
            
        return root
        