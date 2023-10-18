# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 3190

import sys
from collections import deque


input = sys.stdin.readline
n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 'S'

for _ in range(int(input())):
    r, c = map(int, input().split())
    board[r-1][c-1] = 'A'

movements = []
for _ in range(int(input())):
    cnt, direction = map(str, input().split())
    movements.append((int(cnt), direction))

time = 0
queue = deque([(0, 0)])  # 큐에 시작점을 넣는 것이 아니라 뱀의 몸을 모두 저장해야 함
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_idx = 0  # 오른쪽으로 이동(y축으로 +0, x축으로 +1)

while True:
    y, x = queue.popleft()  # 머리
    direction = directions[direction_idx]
    ny, nx = y + direction[0], x + direction[1]
    if ny < 0 or nx < 0 or ny > n - 1 or nx > n - 1:  # 벽에 부딪힘
        break
    if board[ny][nx] == 0:  # 길이를 늘리지 않고 이동
        l = len(queue)
        for _ in range(l):
            by, bx = queue.popleft()  # 이어진 몸이 있는지 확인
            board[y][x] = board[by][bx]
            queue.append((y, x))
            y, x = by, bx
        board[y][x] = 0
        board[ny][nx] = 'S'
        queue.appendleft((ny, nx))

    elif board[ny][nx] == 'A':  # 길이를 늘리고 이동(즉, 꼬리를 그대로 납두고 머리만 늘리기)
        board[ny][nx] = 'S'
        queue.appendleft((y, x))
        queue.appendleft((ny, nx))

    else:
        break  # 자기자신의 몸에 부딪힘
    time += 1
    if movements and time == movements[0][0]:
        if movements[0][1] == 'D':
            direction_idx += 1
        else:
            direction_idx -= 1
        direction_idx %= 4
        movements.pop(0)

print(time + 1)
