# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 프로그래머스 여행 경로

from collections import defaultdict


def solution(tickets):
    global answer
    answer = []
    ticket_dict = defaultdict(list)

    for ticket in tickets:
        ticket_dict[ticket[0]].append(ticket[1])

    for key in ticket_dict:
        ticket_dict[key] = sorted(ticket_dict[key])

    def dfs(city):
        while ticket_dict[city]:
            dfs(ticket_dict[city].pop(0))

        if not ticket_dict[city]:
            answer.append(city)
            return

    dfs('ICN')

    return answer[::-1]
