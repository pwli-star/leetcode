func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for idx, val := range nums{
        if pos2, ok := m[val]; ok{
            return []int{pos2, idx}
        }
        m[target-val] = idx
    }
    return nil
}
