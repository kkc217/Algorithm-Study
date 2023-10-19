# !/usr/env/bin
# -*- coding: utf-8 -*-
# boj 14503

import sys
from collections import deque

input = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

answer = 0
queue = deque([(r, c)])

while queue:
    y, x = queue.popleft()
    if board[y][x] == 0:
        answer += 1
        board[y][x] = 2

    # 4방향 확인
    cleaned = True
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1:
            continue
        if board[ny][nx] == 0:
            cleaned = False
            break

    if cleaned == True:
        ny, nx = y + dy[(d + 2) % 4], x + dx[(d + 2) % 4]  # 후진
        if ny > -1 or nx > -1 or ny < n or nx < m:
            if board[ny][nx] != 1:
                queue.append((ny, nx))

    else:
        find = False
        while not find:
            d = (d - 1) % 4
            ny, nx = y + dy[d], x + dx[d]
            if ny > -1 or nx > -1 or ny < n or nx < m:
                if board[ny][nx] == 0:
                    queue.append((ny, nx))
                    find = True

print(answer)
