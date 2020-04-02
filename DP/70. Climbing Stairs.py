class Solution:
    dp = [-1] * 1000
    def climbStairs(self, n: int) -> int:
        if self.dp[n] > 0 :
            return self.dp[n]
        if n <= 2: 
            self.dp[n] = n
            return n
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.dp[n] = res
        return res
