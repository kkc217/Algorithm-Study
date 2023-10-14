# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2758 로또


# Backtracking 풀이 - 시간 초과
def backtracking(n, m, lotto):
    print(f"backtracking: {lotto}")
    if len(lotto) == n - 1:
        global answer
        # answer += 1
        answer += (m - (lotto[-1] * 2) + 1)
        print(lotto, answer)
        return
    for i in range(lotto[-1]*2, m + 1):
        tmp = i
        for j in range(n - len(lotto) - 1):
            tmp *= 2
            if tmp > m:
                return
        lotto.append(i)
        backtracking(n, m, lotto)
        lotto.pop()


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    answer = 0
    for i in range(1, m + 1):
        if i**n <= m:
            backtracking(n, m, [i])
    print(answer)


# DP 풀이
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(m + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i][j-1]+dp[i-1][j//2]
    print(dp[n][m])
