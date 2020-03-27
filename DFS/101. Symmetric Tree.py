# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.isMirror(root.left, root.right)
        
    def isMirror(self, L, R):
        if not L and not R:
            return True
        if L and not R or R and not L:
            return False
        if L.val == R.val:
            return self.isMirror(L.right, R.left) and self.isMirror(L.left, R.right)
        else:
            return False
