N, M = map(int, input().split())
A, B = [], []

for i in range(N):
    i = list(map(int, input().split()))
    A.append(i)

for i in range(N):
    i = list(map(int, input().split()))
    B.append(i)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
