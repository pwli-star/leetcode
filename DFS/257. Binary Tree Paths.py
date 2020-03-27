# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        self.dfs(root, [], res)
        return res
    
    def dfs(self, root, chan, res):
        if (not root.left) and (not root.right):
            chan.append(root.val)
            res.append('->'.join(map(str, chan.copy())))
            chan.pop()
            return
        chan.append(root.val)
        if root.left:
            self.dfs(root.left, chan, res)
        if root.right:
            self.dfs(root.right, chan, res)
        chan.pop()

            
