# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 아이템 줍기

from collections import deque

def solution(rectangles, characterX, characterY, itemX, itemY):
    answer = 0
    routes = []

    field = [[-1] * 102 for _ in range(102)]

    for rectangle in rectangles:
        x1, y1, x2, y2 = map(lambda x : x * 2, rectangle)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] == 0:
                    field[i][j] = 0
                else:
                    field[i][j] = 1

    character = (characterX * 2, characterY * 2)
    item = (itemX, itemY)
    visited = [[False] * 102 for _ in range(102)]
    queue = deque([character])
    visited[characterX * 2][characterY * 2] = True
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if field[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                field[nx][ny] = field[x][y] + 1

    return field[itemX * 2][itemY * 2] // 2
