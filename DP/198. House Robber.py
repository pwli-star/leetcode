class Solution:
    def rob(self, nums: List[int]) -> int:
        # 状态转移 dp[i+1] = max(dp[i], dp[i-1]+nums[i])
        dp = [-1] * (len(nums)+1)
        return self.f(nums, dp, len(nums))
        
    
    def f(self, nums, dp, n):
        length = len(nums)
        if dp[n] != -1:
            return dp[n]
        if not nums: return 0
        if n == 1: return nums[0]
        if n == 2: return nums[0] if nums[0] > nums[1] else nums[1]
        
        res = max(self.f(nums, dp, n-1), self.f(nums, dp, n-2)+nums[n-1])
        dp[n] = res
        return res
