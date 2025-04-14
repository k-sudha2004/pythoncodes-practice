#FLOORS
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    floor_X = (X - 1) // 10
    floor_Y = (Y - 1) // 10
    print(abs(floor_X - floor_Y))
