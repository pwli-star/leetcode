func thirdMax(nums []int) int {
    s, m, l := math.MinInt64, math.MinInt64, math.MinInt64
    cnt := 0
    for _, v := range nums {
        if v > l {
            cnt += 1
            s, m, l = m, l, v
        } else if v > m && v < l {
            s, m = m, v
            cnt += 1
        } else if v > s && v < m{
            s = v
            cnt += 1
        }
    }
    if cnt > 2 {
        return s
    }
    return l
}
