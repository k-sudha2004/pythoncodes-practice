#CUP FINALS
t=int(input())
for i in range(t):
    X,Y,D=map(int,input().split())
    if abs(X-Y)<=D:
        print("yes")
    else:
        print("no")