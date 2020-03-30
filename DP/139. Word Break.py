class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return False
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if dp[j]:
                    tmp = s[j:i]
                    if tmp in wordDict:
                        dp[i] = True
                        break
        # print(dp)
        return dp[len(s)]
