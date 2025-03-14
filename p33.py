#WATER BOTTELS
T = int(input())

for _ in range(T):
    N, X, K = map(int, input().split())
    max_bottles = min(N, K // X)
    print(max_bottles)
