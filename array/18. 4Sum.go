func fourSum(nums []int, target int) [][]int {
    sort.Ints(nums)
    ret := make([][]int, 0)
    length := len(nums)
    set := make(map[Tuple]struct{})
    for i:=0;i<length-3;i++{
        for j:=i+1;j<length-2;j++{
            left := j + 1
            right := length - 1
            for left<right {
                sum := nums[i] + nums[j] + nums[left] + nums[right]
                if sum > target{
                    right--
                } else if sum < target{
                    left++
                } else {
                    tuple := Tuple{nums[i], nums[j], nums[left], nums[right]}
                    currSeq := [4]int{nums[i], nums[j], nums[left], nums[right]}
                    left++
                    right--
                    if _, ok := set[tuple]; !ok{
                        ret = append(ret, currSeq[:])
                        set[tuple] = struct{}{}
                    }
                }
            }
           
        }
    }
    return ret
}

type Tuple struct{
    a int
    b int
    c int
    d int
}
