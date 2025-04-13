#X JUMPS
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    big_jumps = X // Y
    small_jumps = X % Y
    total_moves = big_jumps + small_jumps
    print(total_moves)
