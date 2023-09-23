# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmer 광물 캐기

from itertools import permutations
from copy import deepcopy

table = {
    "dia": (1, 1, 1),
    "iron": (5, 1, 1),
    "stone": (25, 5, 1)
}

mineral_dict = {
    "diamond": 0,
    "iron": 1,
    "stone": 2
}


# 시간 초과 코드
def solution(picks, minerals):
    answer = 0

    n = len(minerals) // 5
    if len(minerals) % 5 != 0:
        n += 1

    pick_list = []
    pick_list += ['dia' for _ in range(picks[0])]
    pick_list += ['iron' for _ in range(picks[1])]
    pick_list += ['stone' for _ in range(picks[2])]

    answer = 25 * 50

    if len(pick_list) < n:
        n = len(pick_list)

    for pick in set(permutations(pick_list, n)):
        tiredness = 0
        minerals_ = deepcopy(minerals)
        for p in pick:
            for _ in range(5):
                if minerals_:
                    tiredness += table[p][mineral_dict[minerals_.pop(0)]]

        if tiredness < answer:
            answer = tiredness

    return answer


def solution(picks, minerals):
    answer = 0

    # 캘 수 있는 광물의 개수
    if len(minerals) <= sum(picks) * 5:
        n = len(minerals)
    else:
        n = sum(picks) * 5

    print(n)
    mineral_count = []
    tmp = []
    for idx in range(n):
        if idx % 5 == 0:  # 5개마다 초기화
            if tmp:
                mineral_count.append(tmp)
            tmp = [0, 0, 0]

        if minerals[idx] == "diamond":
            tmp[0] += 1
        elif minerals[idx] == "iron":
            tmp[1] += 1
        else:
            tmp[2] += 1
        if idx == n - 1:
            mineral_count.append(tmp)
            break

    mineral_count.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    while mineral_count:
        mineral = mineral_count.pop(0)
        if picks[0] > 0:
            answer += mineral[0] * 1 + mineral[1] * 1 + mineral[2] * 1
            picks[0] -= 1
        elif picks[1] > 0:
            answer += mineral[0] * 5 + mineral[1] * 1 + mineral[2] * 1
            picks[1] -= 1
        else:
            answer += mineral[0] * 25 + mineral[1] * 5 + mineral[2] * 1
            picks[2] -= 1

    return answer
