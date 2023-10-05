INF = 999999999


def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        min_distance = INF
        ballX, ballY = ball

        # 위로 치기
        if ballX == startX and startY < ballY:
            pass
        else:
            oppositeX, oppositeY = startX, n + (n - startY)
            distance = (oppositeX - ballX) ** 2 + (oppositeY - ballY) ** 2
            min_distance = min(distance, min_distance)

        # 아래로 치기
        if ballX == startX and startY > ballY:
            pass
        else:
            oppositeX, oppositeY = startX, -1 * startY
            distance = (oppositeX - ballX) ** 2 + (oppositeY - ballY) ** 2
            min_distance = min(distance, min_distance)

        # 왼쪽으로 치기
        if ballY == startY and startX > ballX:
            pass
        else:
            oppositeX, oppositeY = -1 * startX, startY
            distance = (oppositeX - ballX) ** 2 + (oppositeY - ballY) ** 2
            min_distance = min(distance, min_distance)

        # 오른쪽으로 치기
        if ballY == startY and startX < ballX:
            pass
        else:
            oppositeX, oppositeY = m + (m - startX), startY
            distance = (oppositeX - ballX) ** 2 + (oppositeY - ballY) ** 2
            min_distance = min(distance, min_distance)

        answer.append(min_distance)

    return answer
