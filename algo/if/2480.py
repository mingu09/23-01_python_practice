A, B, C = map(int, input().split())
score = 0


if A == B and B == C:
    score = A * 1000 + 10000
elif A == B:
    score = A * 100 + 1000
elif A == C:
    score = A * 100 + 1000
elif B == C:
    score = B * 100 + 1000
else :
    score = max(A, B, C) * 100

print(score)