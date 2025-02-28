#CARDS
T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    print(min(X, N - X))
