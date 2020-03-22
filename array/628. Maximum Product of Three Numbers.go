func maximumProduct(nums []int) int {
    sort.Ints(nums) // Or, iter to find the max1, max2, max3, min1 and min2
    l := len(nums)
    return max(nums[0]*nums[1]*nums[l-1], nums[l-1]*nums[l-2]*nums[l-3])
}

func max(a, b int) int{
    if a > b {
        return a
    }
    return b
}
