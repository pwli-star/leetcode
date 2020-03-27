# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = [0]
        if not root:
            return res[0]
        self.dfs(root, 0, res)
        return res[0]
    
    def dfs(self, root, tmp, res):
        if not root.left and not root.right:
            tmp = tmp * 10 + root.val
            res[0] += tmp
            tmp = (tmp-root.val)//10
            return
        tmp = tmp * 10 + root.val
        if root.left:
            self.dfs(root.left, tmp, res)
        if root.right:
            self.dfs(root.right, tmp, res)
        tmp = (tmp-root.val)//10
        
