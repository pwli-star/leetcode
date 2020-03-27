# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        res = [2<<31-1]
        if not root:
            return 0
        self.dfs(root, 0, res)
        return res[0]
    
    def dfs(self, root, dep, res):
        if not root.left and not root.right:
            dep += 1
            if dep < res[0]:
                res[0] = dep
            dep -= 1
            return
        dep += 1
        if root.left:
            self.dfs(root.left, dep, res)
        if root.right:
            self.dfs(root.right, dep, res)
        dep -= 1
