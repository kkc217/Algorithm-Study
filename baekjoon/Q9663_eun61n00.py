# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 9663 N-Queen

# 시간 초과

N = int(input())

board = [[0] * N for _ in range(N)]
count = 0


def backtracking(n):
    global count
    if n == N:
        count += 1
        return
    for j in range(N):
        if is_possible(n, j):
            backtracking(n + 1)
            board[n][j] = 0  # 이전 상태로 돌아가기


def is_possible(r, c):
    """
    # i, j에 Queen을 놓을 수 있는지 확인하는 함수
    """

    # 가로 확인
    if 1 in board[r]:
        return False
    # 세로 확인
    for i in range(len(board)):
        if board[i][c] == 1:
            return False

    # 우하향 대각선 확인
    i, j = r, c
    while i > -1 and j > -1:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = r, c
    while i < N and j < N:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    # 우상향 대각선 확인
    i, j = r, c
    while i > -1 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    i, j = r, c
    while i < N and j > -1:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    board[r][c] = 1
    return True


backtracking(0)
print(count)
