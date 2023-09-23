# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 카펫

def solution(brown, yellow):
    answer = []
    div = 0

    while True:
        div += 1
        x, y = yellow // div, div

        if yellow % div != 0:
            continue

        if y > x:
            break

        if (x + y) * 2 + 4 == brown:
            answer = [x + 2, y + 2]
            break

    return answer
