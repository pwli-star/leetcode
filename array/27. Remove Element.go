func removeElement(nums []int, val int) int {
    sort.Ints(nums)
    left := -1 
    right := 0
    for right < len(nums){
        if nums[right] != val {
            left++
            nums[left] = nums[right]
        }
        right++
    }
    return left + 1
}
