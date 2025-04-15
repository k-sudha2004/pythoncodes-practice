#speed limit
T = int(input())
for _ in range(T):
    A, X, B, Y = map(int, input().split())
    speed_alice = A / X
    speed_bob = B / Y

    if speed_alice > speed_bob:
        print("ALICE")
    elif speed_bob > speed_alice:
        print("BOB")
    else:
        print("EQUAL")
