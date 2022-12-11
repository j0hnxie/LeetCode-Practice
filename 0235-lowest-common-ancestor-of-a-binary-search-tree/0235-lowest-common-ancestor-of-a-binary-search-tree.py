# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def lowHelper(self, rootNode, start, end):
            # print(str(rootNode.val) + " " + str(start.val) + " " + str(end.val))
            if rootNode.val <= end.val and rootNode.val >= start.val:
                return rootNode
            elif rootNode.val > end.val:
                return lowHelper(self, rootNode.left, start, end)
            elif rootNode.val < start.val:
                return lowHelper(self, rootNode.right, start, end)
            else:
                print("error")
                
        if p.val < q.val:
            low = p
            high = q
        else:
            low = q
            high = p
        
        return lowHelper(self, root, low, high)
            