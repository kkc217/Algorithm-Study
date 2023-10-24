def solution(n):
    answer = []

    def move(n, src, dest):
        if n == 1:
            answer.append([src, dest])
            return
        move(n-1, src, 6-src-dest)
        move(1, src, dest)
        move(n-1, 6-src-dest, dest)

    move(n-1, 1, 2)
    move(1, 1, 3)
    move(n-1, 2, 3)

    return answer