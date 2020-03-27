# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, chan, res):
        if (not root.left) and (not root.right):
            if sum == root.val:
                chan.append(root.val)
                res.append(chan.copy())
                chan.pop()
            return
        sum -= root.val
        chan.append(root.val)
        if root.left:
            self.dfs(root.left, sum, chan, res)
        if root.right:
            self.dfs(root.right, sum, chan, res)
        chan.pop()

    
