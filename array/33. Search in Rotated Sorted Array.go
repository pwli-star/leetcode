func search(nums []int, target int) int {
    length := len(nums)
    low := 0
    high := length - 1
    // find the smallest value, also the retate position
    for low<high{
        mid := (low+high)/2
        if nums[mid] > nums[high] {
            low = mid + 1
        } else {
            high = mid
        }
    }
    // fmt.Println(low)
    rot := low
    // real binary search
    low = 0
    high = length - 1
    for low <= high {
        mid := (low+high)/2
        realMid := (rot+mid)%length
        // fmt.Println(realMid)
        if nums[realMid] == target{
            return realMid
        } else if nums[realMid] < target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1
}
