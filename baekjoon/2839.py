N = int(input())
"""
if N % 5 == 0:  # 5으로 나눠떨어질 때
    print(N // 5)
else:
    p = 0
    while N > 0:
        N -= 3
        p += 1
        if N % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            p += N // 5
            print(p)
            break
        elif N == 1 or n == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif N == 0:  # 3으로 나눠떨어질 때
            print(p)
            break
"""
count = 0

while N >=0:
    if N % 5 == 0:
        count += int(N//5)
        print(count)
        break
    N -= 3
    count += 1

else:
    print(-1)
