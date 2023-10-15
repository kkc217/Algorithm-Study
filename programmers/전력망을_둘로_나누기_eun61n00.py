# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 전력망을 둘로 나누기

from collections import deque
from copy import deepcopy


# 하나의 전력망에 몇 개의 송전탑이 있는지 세기
def bfs(graph, start):
    count = 1
    queue = deque([start])
    visited = [False] * (len(graph) + 1)
    visited[start] = True

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

        count += 1

    return count


def solution(n, wires):
    answer = 100

    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    for wire in wires:
        graph_ = deepcopy(graph)
        graph_[wire[0]].remove(wire[1])
        graph_[wire[1]].remove(wire[0])

        count1, count2 = bfs(graph_, wire[0]), bfs(graph_, wire[1])

        res = abs(count1 - count2)
        if res < answer:
            answer = res

    return answer
