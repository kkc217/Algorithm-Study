# !/usr/bin/env python
#  -*- coding: utf-8 -*-
# boj 15486 퇴사2

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.insert(0, [0, 0])

# DP 풀이
profit = 0
for i in range(1, n + 1):
    end_date = i + meetings[i][0] - 1  # i일에 시작한 상담이 끝나는 날
    profit = max(profit, dp[i - 1])  # i일까지의 최대 수익
    if end_date <= n:  # 상담이 끝나는 날이 퇴사일을 넘지 않으면
        # 점화식 (현재 저장된 최대 수익과 i-1일까지의 최대 수익 + i일 상담 수익을 비교)
        dp[end_date] = max(dp[end_date], profit+meetings[i][1])

print(max(dp))
