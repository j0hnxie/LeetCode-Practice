# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = [[0, 0, root.val]]
        
        def traverse(root, depth, position, adder):
            # print(str(res[0][0]) + " " + str(res[0][1]) + " " + str(res[0][2]))
            # print(str(depth) + " " + str(position) + " " + str(root.val))
            # print()
            
            if depth >= res[0][0]:
                if depth > res[0][0]:
                    res[0][0] = depth
                    res[0][1] = position
                    res[0][2] = root.val
                    
                if position > res[0][1]:
                    res[0][0] = depth
                    res[0][1] = position
                    res[0][2] = root.val
            if root.left:
                traverse(root.left, depth + 1, position + adder, adder / 2)
            if root.right:
                traverse(root.right, depth + 1, position - adder, adder / 2)
        
        
        traverse(root, 0, 0, 100)
        return res[0][2]
        