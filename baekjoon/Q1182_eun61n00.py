# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1182 부분 수열의 합

from itertools import combinations


n, s = map(int, input().split())
sequence = list(map(int, input().split()))
count = 0

# 풀이 1 백트랙킹을 이용한 풀이


def backtracking(part_sequence, idx):
    global answer, answer_list
    if sum(part_sequence) == s and len(part_sequence) > 0:
        count += 1
    for i in range(idx + 1, len(sequence)):
        num = sequence[i]
        part_sequence.append(num)
        backtracking(part_sequence, i)
        part_sequence.pop()


backtracking([], -1)
print(count)


# 풀이 2 combinations를 이용한 풀이
for i in range(1, n + 1):
    for c in combinations(sequence, i):
        if sum(c) == s:
            count += 1


print(count)
