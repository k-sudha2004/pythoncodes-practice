#CHEF RATINNGS
import math
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())

    if X >= Y:
        print(0)
    else:
        games_needed = math.ceil((Y - X) / 8)
        print(games_needed)
