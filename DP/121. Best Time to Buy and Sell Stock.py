class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = 0
        tmp = 0
        for i in range(len(prices)-1):
            tmp += prices[i+1] - prices[i]
            if (tmp < 0):
                tmp = 0
            res = res if res > tmp else tmp
        return res

