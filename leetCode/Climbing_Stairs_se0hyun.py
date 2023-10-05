class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for step in range(2, n + 1):
            dp.append(dp[step - 2] + dp[step - 1])

        return dp[n]
# n-1번째 계단에서 한 칸 올라가기 + n-2번째 계단에서 두 칸 올라가기