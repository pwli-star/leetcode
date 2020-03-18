func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    str := strconv.Itoa(x)
    right := len(str)
    left := 0
    for right > left{
        if str[left] != str[right-1]{
            return false
        }
        left++
        right--
    }
    return true
}
