func maxArea(height []int) int {
    max := -1
    length := len(height)
    left, right := 0, length - 1
    for left < right{
        tmp := (right-left)*min(height[left], height[right])
        if tmp > max{
            max = tmp
        }
        if height[left] < height[right]{
            left += 1
        } else {
            right -= 1
        }
    }
    return max
}

func min(a, b int) int{
    if a <= b{
        return a
    }
    return b
}
