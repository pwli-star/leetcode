/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    if root == nil {
        return true
    }
    lDepth := depth(root.Left)
    rDepth := depth(root.Right)
    return abs(lDepth-rDepth) < 2 && isBalanced(root.Left) && isBalanced(root.Right)
}

func depth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    return max(depth(root.Left), depth(root.Right))+1
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}

func abs(a int) int{
    if a < 0{
        a = -a
    }
    return a
}
