# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14499

import sys

input = sys.stdin.readline
dice = [[0], [0, 0, 0], [0], [0]]

n, m, y, x, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 동, 서, 북, 남
dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)

for movement in list(map(int, input().split())):
    nx, ny = x + dx[movement - 1], y + dy[movement - 1]
    if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
        continue
    if movement == 4:
        dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[3][0], dice[0][0], dice[1][1], dice[2][0]
    elif movement == 3:
        dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[1][1], dice[2][0], dice[3][0], dice[0][0]
    elif movement == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][0] = dice[1][1], dice[1][2], dice[3][0], dice[1][0]
    else:
        dice[1][0], dice[1][1], dice[1][2], dice[3][0] = dice[3][0], dice[1][0], dice[1][1], dice[1][2]

    if board[ny][nx] == 0:
        board[ny][nx] = dice[3][0]
    else:
        dice[3][0] = board[ny][nx]
        board[ny][nx] = 0
    x, y = nx, ny
    print(dice[1][1])
