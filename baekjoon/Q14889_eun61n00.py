# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14889

from itertools import combinations

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]

answer = 999999999
for combination in combinations([i for i in range(n)], n//2):
    star = list(combination)
    link = [i for i in range(n) if i not in star]

    star_power = 0
    link_power = 0
    for comb2 in combinations(star, 2):
        star_power += power[comb2[0]][comb2[1]]
        star_power += power[comb2[1]][comb2[0]]
    for comb2 in combinations(link, 2):
        link_power += power[comb2[0]][comb2[1]]
        link_power += power[comb2[1]][comb2[0]]

    answer = min(answer, abs(star_power - link_power))

print(answer)
