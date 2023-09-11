# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 프로그래머스 소수 찾기

import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if is_prime(i) == True:
            answer += 1
    return answer
