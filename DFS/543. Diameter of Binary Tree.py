# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.ht(root)
        
        return self.res
    
    def ht(self, root):
        if not root: 
            return 0
        l = self.ht(root.left)
        r = self.ht(root.right)
        self.res = max(self.res, l+r)
        return 1 + max(l, r)
        
