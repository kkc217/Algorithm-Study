# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 모음 사전

from itertools import product


def solution(word):
    answer = []
    list = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        for per in product(list, repeat=i):
            answer.append(''.join(per))

    answer.sort()
    return answer.index(word) + 1
