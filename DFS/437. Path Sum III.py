# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    def dfs(self, root, sum):
        if not root: return 0
        return self.dfs(root.left, sum-root.val) + self.dfs(root.right, sum-root.val) + (1 if root.val == sum else 0)
