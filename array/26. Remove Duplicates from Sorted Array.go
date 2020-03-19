func removeDuplicates(nums []int) int {
    if len(nums) <= 1{
        return len(nums)
    }
    left := 0
    right := 1
    for right<len(nums) {
        if nums[left]==nums[right]{
            right++
        } else {
            left++
            nums[left] = nums[right]
        }
    }
    
    return left + 1
}
