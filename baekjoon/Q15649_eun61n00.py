# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15649 N과 M(1)

from itertools import permutations

n, m = map(int, input().split())

num_list = [_ for _ in range(1, n + 1)]

for p in permutations(num_list, m):
    print(*p)
