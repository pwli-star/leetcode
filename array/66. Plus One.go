func plusOne(digits []int) []int {
    length := len(digits)
    ret := make([]int, length+1)
    div, mod := 0, 0
    for i:=length-1;i>=0;i--{
        tmp := digits[i]
        if i==length-1{ 
            tmp = digits[i] + 1
        }
        if div!=0{
            tmp += 1
            div, mod = 0, 0
        }
        if tmp > 9{
            div, mod = 1, tmp%10
            ret[i+1] = mod
        } else{   
            ret[i+1] = tmp
        }
    }
    if div!=0 {
        ret[0]+= 1
    }
    if ret[0] == 0{
        ret = ret[1:]
    }
    return ret
}

