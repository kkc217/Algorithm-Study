# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1759 암호 만들기

l, c = map(int, input().split())
characters = list(map(str, input().split()))
characters.sort()


def backtracking(password, idx):
    if is_possible(password):
        print(password)

    for i in range(idx + 1, len(characters)):
        password += characters[i]
        backtracking(password, i)
        password = password[:-1]


def is_possible(password):
    abc, aeiou = 0, 0
    for i in password:
        if i in ["a", "e", "i", "o", "u"]:
            aeiou += 1
        else:
            abc += 1
    if abc >= 2 and aeiou >= 1 and len(password) == l:
        return True
    return False


backtracking("", -1)
