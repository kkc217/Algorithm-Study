# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1012 유기농 배추

import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, field, visited):
    n, m = len(visited), len(visited[0])
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            elif field[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])

    return visited


for _ in range(t):
    answer = 0
    m, n, k = map(int, input().split())
    field = [[0] * m for __ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for __ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1
    for x in range(n):
        for y in range(m):
            if field[x][y] == 1 and not visited[x][y]:
                visited = bfs(x, y, field, visited)
                answer += 1

    print(answer)
