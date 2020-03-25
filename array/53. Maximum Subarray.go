func maxSubArray(nums []int) int {
    ret := math.MinInt32
    sum := 0
    for _, v := range nums{
        sum += v
        if sum > ret{
            ret = sum
        }
        if sum < 0{
            sum = 0
        }
    }
    return ret
}


