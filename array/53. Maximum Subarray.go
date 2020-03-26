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



/* 
// solution 2：
// divide and conquer

func maxSubArray(nums []int) int {
    return divideAndConquer(nums, 0, len(nums)-1)
}

func divideAndConquer(nums []int, left, right int) int{
    if left == right{
        return nums[left]
    }
    mid := (left+right)/2
    lMax := divideAndConquer(nums, left, mid)
    rMax := divideAndConquer(nums, mid+1, right)
    crossLeft := math.MinInt32
    crossRight := math.MinInt32
    crossSum := 0
    for i:=mid;i>=left;i--{
        crossSum += nums[i]
        if crossSum > crossLeft{
            crossLeft = crossSum
        }
    }
    crossSum = 0
    for i:=mid+1;i<=right;i++{
         crossSum += nums[i]
        if crossSum > crossRight{
            crossRight = crossSum
        }
    }
    return max(lMax, rMax, crossLeft+crossRight)
}

func max(args ...int) int{
    ret := math.MinInt32
    for _, v := range args{
        if v > ret{
            ret = v
        }
    }
    return ret
}

*/
