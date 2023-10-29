from itertools import product


def solution(users, emoticons):
    answer = []
    discounts = [10, 20, 30, 40]

    for case in product(discounts, repeat=len(emoticons)):
        # 이모티콘 플러스 서비스 가입자와 판매액 계산
        emoticon_plus_count = 0
        total_purchase = 0
        for user in users:
            ratio, price = user[0], user[1]
            purchase_price = sum([emoticons[idx] * (1 - case_item * 0.01)
                                 for idx, case_item in enumerate(case) if case_item >= ratio])
            if purchase_price >= price:
                emoticon_plus_count += 1
            else:
                total_purchase += purchase_price

        answer.append((emoticon_plus_count, total_purchase))

    answer.sort(reverse=True)
    return answer[0]
