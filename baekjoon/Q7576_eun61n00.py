# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 7576 토마토

import sys
from collections import deque

input = sys.stdin.readline

m, n, o = map(int, input().split())

graph = [[] for _ in range(o)]
visited = [[[False] * m for _ in range(n)] for _ in range(o)]

tomato_idx = []

for i in range(o):
    for j in range(n):
        tomatoes = list(map(int, input().split()))
        graph[i].append(tomatoes)
        for k, tomato in enumerate(tomatoes):
            if tomato == 1:
                tomato_idx.append((k, j, i))


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
answer = 0


def bfs(graph, start, visited):
    global answer
    queue = deque([])
    for s in start:
        x, y, h = s
        queue.append((x, y, h))
        visited[h][y][x] = True

    while queue:
        x, y, h = queue.popleft()

        for i in range(6):
            nx, ny, nh = x+dx[i], y+dy[i], h+dh[i]

            if nx < 0 or ny < 0 or nh < 0 or nx >= m or ny >= n or nh >= o:
                continue
            if visited[nh][ny][nx] == False and graph[nh][ny][nx] == 0:
                graph[nh][ny][nx] = graph[h][y][x] + 1
                answer = max(answer, graph[nh][ny][nx])
                queue.append((nx, ny, nh))
                visited[nh][ny][nx] = True

    return graph


graph = bfs(graph, tomato_idx, visited)


# 안익은 토마토가 있음에도 익히지 못함
for h in graph:
    if any(0 in i for i in h):
        answer = -1
        break

if answer > 0:  # 첫날은 정답에서 빼기
    answer -= 1
elif answer == 0:  # 익힌 토마토가 없음
    answer = 0

print(answer)
