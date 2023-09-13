# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1476 날짜 계산

e, s, m = map(int, input().split())
answer = 1

while True:
    if (answer - e) % 15 == 0 and (answer - s) % 28 == 0 and (answer - m) % 19 == 0:
        break
    answer += 1

print(answer)
