# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# programmers 요격 시스템

def solution(targets):
    answer = 0

    targets.sort()
    bound = 0
    for target in targets:
        s, e = target

        # 요격 가능
        if s < bound:
            bound = min(bound, e)

        # 요격 불가능
        else:
            answer += 1
            bound = e

    return answer
