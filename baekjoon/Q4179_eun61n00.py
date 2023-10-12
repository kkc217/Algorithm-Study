# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 4179 불!

import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int, input().split())
visited = [[False] * w for _ in range(h)]

graph = []
for _ in range(h):
    graph.append(list(input())[:w])

fire_start = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == "J":
            jihoon_start = (i, j)
            graph[i][j] = 0
        elif graph[i][j] == "F":
            fire_start.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0


def fire_bfs(start):
    global graph, w, h
    fire = deque([])
    visited = [[False] * w for _ in range(h)]
    for s in start:
        y, x = s
        fire.append((y, x))
        visited[y][x] = True

    while fire:
        y, x = fire.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or nx < 0 or ny > h - 1 or nx > w - 1:
                continue
            if visited[ny][nx] == False and graph[ny][nx] != "#":
                graph[ny][nx] = graph[y][x] + "F"
                visited[ny][nx] = True
                fire.append((ny, nx))


def jihoon_bfs(start):
    global graph, w, h
    y, x = start
    jihoon = deque([(y, x)])
    graph[y][x] = 0
    visited = [[False] * w for _ in range(h)]
    visited[y][x] = True

    while jihoon:
        y, x = jihoon.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or nx < 0 or ny > h - 1 or nx > w - 1:
                return graph[y][x] + 1
            if visited[ny][nx] == False and graph[ny][nx] != "#":
                if graph[ny][nx] == "." or graph[ny][nx].count("F") - 1 > graph[y][x] + 1:
                    visited[ny][nx] = True
                    jihoon.append((ny, nx))
                    graph[ny][nx] = graph[y][x] + 1

    return -1


fire_bfs(fire_start)
answer = jihoon_bfs(jihoon_start)
if answer > -1:
    print(answer)
else:
    print("IMPOSSIBLE")
