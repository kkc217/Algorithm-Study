# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 과제 진행하기

def solution(plans):
    complete_plans = []

    for plan in plans:
        hh, mm = plan[1].split(":")
        plan[1] = int(hh) * 60 + int(mm)
        plan[2] = int(plan[2])

    plans.sort(key=lambda x: x[1])

    current_time = plans[0][1]
    not_started_plan = plans
    stopped_plan = []

    while not_started_plan:
        name, start, playtime = not_started_plan.pop(0)

        # 마지막 과제가 아니면
        if not_started_plan:
            next_name, next_start, next_playtime = not_started_plan[0]

            # 중단
            if start + playtime > next_start:
                stopped_plan.append(
                    [name, start, playtime - (next_start - start)])

            else:
                complete_plans.append(name)
                remain = (next_start - start) - playtime

                # 과제 다 하고도 시간 남음
                while remain > 0 and stopped_plan:
                    stop_name, stop_start, stop_playtime = stopped_plan.pop(-1)
                    if stop_playtime > remain:
                        stopped_plan.append(
                            [stop_name, stop_start, stop_playtime - remain])
                    else:
                        complete_plans.append(stop_name)
                    remain -= stop_playtime

        else:
            complete_plans.append(name)

    while stopped_plan:
        complete_plans.append(stopped_plan.pop(-1)[0])

    return complete_plans
