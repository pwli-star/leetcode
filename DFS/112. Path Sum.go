/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, sum int) bool {
    if root == nil{
        return false
    }
    res := make([]bool, 1)
    dfs(root, sum, res)
    return res[0]
}

func dfs(root *TreeNode, sum int, res []bool) {
    if root.Left == nil && root.Right == nil{
        if sum == root.Val{
            res[0] = true
        }
        return
    }
    sum -= root.Val
    if root.Left != nil{
        dfs(root.Left, sum, res)
    }
    if root.Right != nil{
        dfs(root.Right, sum, res)
    }
}
