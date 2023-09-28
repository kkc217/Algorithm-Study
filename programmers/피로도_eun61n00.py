# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 피로도


from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for case in permutations(dungeons, len(dungeons)):

        # 각 케이스 별 탐험 가능 던전 수 확인
        tired = k
        count = 0
        for min_tired, use_tired in case:
            if tired < min_tired:
                break
            tired -= use_tired
            count += 1

        # 최대값 업데이트
        if count > answer:
            answer = count

    return answer
