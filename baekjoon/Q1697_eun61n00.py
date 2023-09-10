# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1697 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
visited = [False] * 1000001

queue = deque([])
queue.append([n, 0])
while queue:
    i, cnt = queue.popleft()
    if i == k:
        answer = cnt
        break
    if 0 <= i - 1 <= 1000000 and not visited[i - 1]:
        visited[i - 1] = True
        queue.append([i - 1, cnt + 1])
    if 0 <= i + 1 <= 1000000 and not visited[i + 1]:
        visited[i + 1] = True
        queue.append([i + 1, cnt + 1])
    if 0 <= i * 2 <= 100000 and not visited[i * 2]:
        visited[i * 2] = True
        queue.append([i * 2, cnt + 1])

print(answer)
