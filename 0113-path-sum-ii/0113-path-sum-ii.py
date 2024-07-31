# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(node, path, cur_sum):
            if not node:
                return
            
            path = path + [node.val]
            cur_sum = cur_sum + node.val

            dfs(node.left, path, cur_sum)
            dfs(node.right, path, cur_sum)

            if not node.left and not node.right:
                if cur_sum == targetSum:
                    self.res.append(path)
        
        dfs(root, [], 0)
        return self.res