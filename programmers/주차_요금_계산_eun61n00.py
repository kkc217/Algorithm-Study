from collections import defaultdict
from math import ceil


def solution(fees, records):
    answer = defaultdict(int)
    fee_list = []
    record_dict = {}
    base_time, base_fee, unit_time, unit_fee = int(
        fees[0]), int(fees[1]), int(fees[2]), int(fees[3])

    for record in records:
        # 05:34 5961 IN
        time, number, IN = record.split(' ')
        hh, mm = time.split(':')
        IN = True if IN == "IN" else False
        if number in record_dict.keys():
            # 주차 요금 계산
            parking_time = (int(hh) * 60 + int(mm)) - \
                (record_dict[number][0] * 60 + record_dict[number][1])

            answer[number] += parking_time
            del (record_dict[number])

        else:
            record_dict[number] = (int(hh), int(mm))

    for number in record_dict.keys():
        parking_time = (23 * 60 + 59) - \
            (record_dict[number][0] * 60 + record_dict[number][1])
        answer[number] += parking_time

    for ans in answer.keys():
        number = int(ans)
        parking_time = answer[ans]
        if parking_time <= base_time:
            parking_fee = base_fee
        else:
            parking_fee = base_fee
            parking_time -= base_time
            parking_fee += ceil(parking_time / unit_time) * unit_fee
        fee_list.append((number, parking_fee))

    fee_list.sort()
    return [row[1] for row in fee_list]
