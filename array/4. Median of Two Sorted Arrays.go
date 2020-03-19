func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    len1 := len(nums1)
    len2 := len(nums2)
    i, j := 0, 0
    arr := make([]int, 0)
    for ;i<len1&&j<len2;{
        if nums1[i] < nums2[j]{
            arr = append(arr, nums1[i])
            i++
        } else {
            arr = append(arr, nums2[j])
            j++
        }
    }
    if i==len1 {
        arr = append(arr, nums2[j:]...)
    } else {
        arr = append(arr, nums1[i:]...)
    }
    mid := (len1+len2)/2
    // fmt.Println(mid, arr)
    if (len1+len2)%2!=0 {
        return float64(arr[mid])
    }
    return (float64(arr[mid-1])+float64(arr[mid]))/2.0
}
