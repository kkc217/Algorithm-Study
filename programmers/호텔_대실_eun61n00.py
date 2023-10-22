import heapq


def solution(book_time):

    for idx, time in enumerate(book_time):
        start_time, end_time = time
        hh_s, mm_s = start_time.split(":")
        hh_e, mm_e = end_time.split(":")
        book_time[idx] = [int(hh_s) * 60 + int(mm_s),
                          int(hh_e) * 60 + int(mm_e) + 10]

    book_time.sort()  # 시작순으로 정렬
    rooms = [book_time[0][1]]  # rooms에는 끝나는 시간만 저장
    for time in book_time[1:]:
        start, end = time
        need_room = True
        for idx, room in enumerate(rooms):
            if start >= room:
                need_room = False
                rooms[idx] = end
                break
        if need_room:
            rooms.append(end)

    print(rooms)
    return len(rooms)
