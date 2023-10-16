# Clipper 3주차

N, k = map(int, input().split())
scores = map(int, input().split())

scores = sorted(scores, reverse=True)
print(scores[k-1])