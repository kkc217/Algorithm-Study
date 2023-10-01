# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1182 부분 수열의 합

from itertools import combinations


n, s = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

# 풀이 1 백트랙킹을 이용한 풀이 (정답 X)


def back_tracking(lst, idx):
    global count
    if lst and sum(lst) == s:
        print(lst)
        count += 1
        return
    for i in range(num_list[idx], n):
        if num_list[i] not in lst:
            lst.append(num_list[i])
            print(idx, lst)
            back_tracking(lst, idx + 1)
            lst.pop()


back_tracking([], 0)
print(count)


# 풀이 2 combinations를 이용한 풀이
for i in range(1, n + 1):
    for c in combinations(num_list, i):
        if sum(c) == s:
            count += 1


print(count)
