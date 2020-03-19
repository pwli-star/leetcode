func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	// fmt.Println(nums)
	length := len(nums)
	ret := make([][]int, 0)
	set := make(map[Tuple]struct{})
	for i := 0; i < length-2; i++ {
		left := i + 1
		right := length - 1
		for left < right {
			sum := nums[i] + nums[left] + nums[right]
			if sum > 0 {
				right--
			} else if sum < 0 {
				left++
			} else {
				currSeq := [3]int{nums[i], nums[left], nums[right]}
				tuple := Tuple{nums[i], nums[left], nums[right]}
				left++
				right--
				if _,ok:=set[tuple]; ok {
					continue
				}
				ret = append(ret, currSeq[:])
				set[tuple] = struct{}{}
			}
		}
	}

	return ret
}

type Tuple struct {
	a int
	b int
	c int
}
