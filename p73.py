#chef eren
T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    odd = (N + 1) // 2
    even = N // 2
    total_duration = (odd * B) + (even * A)
    print(total_duration)
