# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15649 N과 M(1)

from itertools import permutations

n, m = map(int, input().split())

# 풀이 1(파이썬 라이브러리 사용)
num_list = [_ for _ in range(1, n + 1)]

for p in permutations(num_list, m):
    print(*p)


# 풀이 2 (백트랙킹)
answer = []


def backtracking():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, n + 1):
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()


backtracking()
