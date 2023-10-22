# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14500

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def dfs(board, y, x, visited, values, lst):
    # dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    dx, dy = [-1, 1, 0], [0, 0, 1]
    global answer, max_value

    if len(values) == 4:
        answer = max(answer, sum(values))
        return

    if ((4 - len(values)) * max_value) + sum(values) <= answer:
        return

    if len(lst) == 3 and (lst[0][1] == lst[1][1] == lst[2][1]):
        for i in [-1, 1]:
            ny, nx = lst[1][0], lst[1][1] + i
            if nx < 0 or nx > m - 1:
                continue
            answer = max(answer, sum(values) + board[ny][nx])
            visited[ny][nx] = True

    elif len(lst) == 3 and (lst[0][0] == lst[1][0] == lst[2][0]):
        for i in [-1, 1]:
            ny, nx = lst[1][0] + i, lst[1][1]
            if ny < 0 or ny > n - 1:
                continue
            answer = max(answer, sum(values) + board[ny][nx])
            visited[ny][nx] = True

    for i in range(3):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1:
            continue
        if not visited[ny][nx]:
            visited[ny][nx] = True
            values.append(board[ny][nx])
            lst.append((ny, nx))
            dfs(board, ny, nx, visited, values, lst)
            visited[ny][nx] = False
            values.pop()
            lst.pop()


def check_square(board, y, x):
    global answer
    dy = (-1, -1, 1, 1)
    dx = (-1, 1, -1, 1)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1:
            continue
        answer = max(answer, board[ny][nx] + board[y][nx] +
                     board[ny][x] + board[y][x])


answer = 0

max_value = max(map(max, board))
for y in range(n):
    for x in range(m):
        visited = [[False] * m for _ in range(n)]
        visited[y][x] = True
        dfs(board, y, x, visited, [board[y][x]], [(y, x)])
        # check_square(board, y, x)

print(answer)
