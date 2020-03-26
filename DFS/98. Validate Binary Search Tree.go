/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var vals []int

func isValidBST(root *TreeNode) bool {
    if root == nil {
        return true
    }
    vals = make([]int, 0)
    midTriviale(root)
    curr := vals[0]
    for _, v := range vals[1:]{
        if curr >= v{
            return false
        }
        curr = v
    }
    return true
}

func midTriviale(root *TreeNode) {
    if root == nil{
        return
    }
    if root.Left != nil {
        midTriviale(root.Left)
    }
    vals = append(vals, root.Val)
    if root.Right != nil {
        midTriviale(root.Right)
    }
}
