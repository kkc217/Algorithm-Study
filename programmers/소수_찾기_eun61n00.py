# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 프로그래머스 소수 찾기

from itertools import permutations
from collections import defaultdict
import math

check = defaultdict(bool)


def is_prime(x):
    if x == 0 or x == 1:
        return 0

    if check[x] == True:
        return 0

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0

    check[x] = True
    return 1


def solution(numbers):
    answer = 0
    num_list = [ch for ch in numbers]

    for n in num_list:
        answer += is_prime(int(n))

    for i in range(2, len(numbers) + 1):
        comb = list(permutations(num_list, i))
        for c in comb:
            n = int(''.join(c))
            answer += is_prime(n)

    return answer
