# MARIO AND BULLET
t=int(input())
for i in range(t):
    X,Y,Z=map(int,input().split())
    bullet=Y//X
    if bullet>Z:
        print(0)
    else:
        print(Z-bullet)