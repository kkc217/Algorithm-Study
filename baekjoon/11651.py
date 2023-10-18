# Clipper 3주차

N = int(input())

metrics = []
for i in range(N):
    x, y = map(int, input().split())
    metrics.append([x, y])

metrics.sort(key=lambda x:(x[1], x[0]))

for i in metrics:
    print(i[0], i[1])