func threeSumClosest(nums []int, target int) int {
    sort.Ints(nums)
    length := len(nums)
    ret := nums[0] + nums[1] +nums[length-1]
    for i:=0;i<length-2;i++{
        left := i + 1
        right := length - 1
        for left < right{
            sum := nums[i] + nums[left] + nums[right]
            if sum  < target{
                left++
            } else {
                right--
            }
            if abs(sum-target) < abs(ret-target){
                ret = sum
            }
        }
    }
    return ret
}

func abs(a int) int{
    if a < 0 {
        return -a
    }
    return a
}
