import sys
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 작은 값에 사서 높은 값에 팔기
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)

        return profit